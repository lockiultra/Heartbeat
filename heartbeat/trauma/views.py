from django.shortcuts import render
from django.views.generic import TemplateView
from trauma.forms import PromptForm
from trauma.utils.lstm import get_predict

# Create your views here.

class TraumaView(TemplateView):
    template_name = 'trauma/trauma_index.html'

class TraumaLSTMView(TemplateView):
    template_name = 'trauma/trauma_lstm.html'
    
    def get(self, request, *args, **kwargs):
        form = PromptForm()
        return render(request, 'trauma/trauma_lstm.html', {'form': form, 'result': 'None'})
    
    def post(self, request, *args, **kwargs):    
        prompt = request.POST['prompt']
        predict = int(get_predict(prompt)[0])
        form = PromptForm()
        return render(request, 'trauma/trauma_lstm.html', {'form': form, 'result': predict})