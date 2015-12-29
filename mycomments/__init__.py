from threadedcomments.models import ThreadedComment
from .forms import MyCommentForm

def get_model():
    return ThreadedComment

def get_form():
    return MyCommentForm