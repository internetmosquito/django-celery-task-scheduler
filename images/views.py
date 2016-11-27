from django.views.generic.list import ListView

from images.models import Image


class ImageView(ListView):
    model = Image
    template_name = 'images/images_list.html'
    paginate_by = 24

    # def get_context_data(self, **kwargs):
    #     context = super(PhotoView, self).get_context_data(**kwargs)
    #     context['form'] = FeedbackForm()
    #     return context
