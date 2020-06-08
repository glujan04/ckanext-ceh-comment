import logging
import ckan.logic as logic

from ckan.lib.base import abort

import ckanext.ceh_comment.model as comment_model

log = logging.getLogger(__name__)


def thread_read(context, data_dict):
    model = context['model']

    #logic.check_access("thread_read", context, data_dict)

    # otherwise content should be set to withdrawn text
    id = logic.get_or_bust(data_dict, 'id')
    commentThread = comment_model.CommentThread.get(id)
    if not commentThread:
        abort(404)

    commentThread.active_thread = 'active'

    model.Session.add(commentThread)
    model.Session.commit()

    return {'success': True}