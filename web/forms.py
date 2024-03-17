from django import forms
from .models import Ticket, Message

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'ticketPhone': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'ticket-form-phone',
                'placeholder': "Ph 085-456-7890",
                'pattern': "[0-9]{3}-[0-9]{3}-[0-9]{4}",

            }),
            'ticketFullName': forms.TextInput(attrs={
                'name': 'ticket-form-name',
                'id': 'ticket-form-name',
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'ticketEmail': forms.TextInput(attrs={
                'name': 'ticket-form-email',
                'id': 'ticket-form-email',
                'class': 'form-control',
                'placeholder': 'Email address',
                'pattern': "[^ @]*@[^ @]*"
            }),
            'ticketType': forms.RadioSelect(attrs={
                'name':'TicketForm',
                'id': 'flexRadioDefault',
                'class': 'form-check-input'
            }, choices=Ticket.type),
            'ticketRequest': forms.Textarea(attrs={
                'name': 'ticket-form-message',
                'id': 'ticket-form-message',
                'class': 'form-control',
                'placeholder': 'Additional Request',
                'rows': '3'
            })
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'messageFullName' : forms.TextInput(attrs={
                'name' : 'contact-name',
                'class': 'form-control',
                'placeholder': 'Full name'
            }),
            'messageEmail' : forms.TextInput(attrs={
                'name': 'contact-email',
                'pattern': '[^ @]*@[^ @]*',
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'messageSuggestion': forms.Textarea(attrs={
                'name': 'contact-message',
                'rows': '3',
                'class': 'form-control',
                'placeholder': 'Message'
            })
        }