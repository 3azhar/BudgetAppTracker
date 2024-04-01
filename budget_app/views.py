from django.shortcuts import render
from . models import Transaction , Entry
from django.http import HttpResponseRedirect
from django.urls import reverse

from . forms import EntryForm
import plotly.express as px
import pandas as pd



# Create your views here.

def index (request):
    """Home page"""
    return render(request, 'budget_app/index.html')

def transactions(request):
    """Showing transactions"""
    transactions = Transaction.objects.order_by('date_added')
    context = {'transactions': transactions}
    return render(request,'budget_app/transactions.html', context)

def transaction(request, transaction_id):
    """Showing single transactions and all entries"""
    transaction = Transaction.objects.get(id=transaction_id)
    entries = transaction.entry_set.order_by('-date_added')
    context = {'transaction': transaction, 'entries': entries}
    return render(request,'budget_app/transaction.html', context)



def new_entry(request, transaction_id):
    """Add new entry for a particular transaction"""
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method != 'POST':
       #no data submitted (creates blank form) 
       form = EntryForm()
    else:
        #POST Data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.transactions = transaction
            new_entry.save()
            return HttpResponseRedirect(reverse('budget_app:transaction', args=[transaction_id]))
    context = {'transaction': transaction, 'form': form}
    return render(request, 'budget_app/new_entry.html', context)

def bar_chart(request):
    """Show/design the bar chart"""
    transactions =  Transaction.objects.all()
    transaction_amount = [(transaction.TransactionType, sum(entry.transaction_amount for entry in transaction.entry_set.all())) for transaction in transactions]
    df = pd.DataFrame(transaction_amount, columns=['Transaction Type', 'Transaction Amount'])
    fig = px.bar(df, x='Transaction Type', y='Transaction Amount', color = 'Transaction Type')
    fig.update_yaxes(tickformat='d', dtick=10)
    chart_html = fig.to_html()
    context = {'chart_html': chart_html}
    return render(request, 'budget_app/bar_chart.html', context)

def delete(request, entry_id):
    """Delete specific topic"""
    Entry.objects.filter(id=entry_id).delete()
    return HttpResponseRedirect(reverse('budget_app:transactions'))