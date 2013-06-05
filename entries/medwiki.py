# -*- coding: utf-8 -*-

"""
Functions to interact with wikipedia.
"""

from datetime import datetime
import mwclient
from django.conf import settings



_source_wikipedia = getattr(settings, 'SOURCE_WIKI', 'debian-wiki')
_target_wikipedia = getattr(settings, 'TARGET_WIKI', 'debian-wiki')
_api_path = getattr(settings, 'API_PATH', '/wiki/')
_summary_text = getattr(settings, 'SUMMARY_TEXT', 'Translated with Transifex, '
    'the Open Translation Platform')



def get_original_article(title, credentials=None):
    """Get the content of an article from the english wikipedia.

    Args:
        title: The title of the article (the part after the http://host/wiki/).
    Returns:
        The user-editable content of the article.
    """
    
    page = _get_page(_source_wikipedia, title, credentials)
    content = page.edit()
    revision = page.revision
    return content, revision


def push_translated_article(title, content, credentials):
    """Push a translated article to the Greek wikipedia.

    Args:
        title: The title of the article to save
            (the part after http://host/wiki/).
    Returns:
        The new revision ID of the saved page or
        False if the page was not updated.
    """
    
    page = _get_page(_target_wikipedia, title, credentials)
    saved = page.save(content, summary=_summary_text)

    if 'nochange' in saved:
        return False

    if 'newrevid' in saved:
        add_to_discussion(
            title, "Updated by Transifex %s" % datetime.now(), credentials
        )
        return saved['newrevid']

    return False


def add_to_discussion(title, content, credentials):
    """Add an entry to the discussion page of the specified article.

    TODO: Maybe add a labeled section in discussion pages for Transifex
    submissions.

    Args:
        title: The title of the article.
        content: Discussion text to add.
    Returns:
        The new revision ID of the saved page or
        False if the page was not updated.
    """
    discussion_title = 'Talk:%s' % title
    current_content, r = get_original_article(discussion_title, credentials)
    return push_translated_article(
        discussion_title,
        '%s\n\n%s' % (current_content, content),
        credentials
    )


def is_article_updated(title, saved_revision, credentials=None):
    """Check whether an article has been updated.

    Check the last revision of the article against the saved one. Assume,
    that the article in the Wikipedia is always newer than the one saved
    in Transifex.

    Args:
        title: The title of the article to save.
        saved_revision: The revision of the article that has been saved.
    Returns:
        The latest revision, if the article has been updated since the last
        time it was saved. Else False.
    """
    page = _get_page(_source_wikipedia, title, credentials)
    current_revision = page.revision
    return current_revision if current_revision != saved_revision else False


def is_article_manually_edited(title, saved_revision, credentials=None):
    """Check whether an article has been changed manually in the target
    mediawiki.

    Args:
        title: The title of the article.
        saved_revision: The revision ofthe article that has been saved.
    Returns:
        True, if the article has been edited manually. Else, False.
    """
    page = _get_page(_target_wikipedia, title, credentials)
    current_revision = page.revision
    if saved_revision is not None:
        return current_revision != saved_revision
    else:
        return False


def _get_page(wiki, title, credentials):
    """Get a reference to an artile in the wiki.

    Args:
        wiki: The wiki that hosts the article.
        title: The title of the article.
    Returns:
        A Page object of the mwclient.
    """
    site = mwclient.Site(wiki, path=_api_path)
    if credentials is not None:
        site.login(credentials.get('username'), credentials.get('password'))
    return site.Pages[title]

