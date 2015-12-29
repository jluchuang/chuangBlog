#!/usr/bin python
# coding=utf-8

from crispy_forms.helper import FormHelper
from threadedcomments.forms import ThreadedCommentForm as base_class

class MyCommentForm(base_class):
    """My Customized Comment Form.

    Just add some features via crispy.
    """

    #: Helper for {% crispy %} template tag
    helper = FormHelper()
    helper.form_tag = False