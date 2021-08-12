from Finance.models import User,Transaction
from Finance.forms import TransactionForm, UserForm
from django.shortcuts import render,redirect
from django.forms.formsets import formset_factory
from django.db.models import Sum
# Create your views here.
# Use formser.factory to join table.
#request object contain two methods GET and POST. First of them use to get value from table, second to post value.

def add_transaction(request):
    TransactionFormSet = formset_factory(TransactionForm, extra = 10, min_num=1, validate_min = True)
    if(request.method == 'POST'):
        user_form = UserForm(request.POST)
        transaction_formset = TransactionForm(request.POST)
#validation data
        if all([user_form.is_valid() , transaction_formset.is_valid()]):
            user = user_form.save()
            for inline_form in transaction_formset:
#cleaned data, change to appropriate type
                if inline_form.cleaned_data:
                    transaction = inline_form.save(commit=False)
                    transaction.user_id = user
                    transaction.save()
#rendering page, concrete index.html
            return render(request,'Finance/index.html', {})
        else:
            user_form = UserForm()
            transaction_formset = TransactionForm()
    return render(request,'Finance/add_transaction.html', {
        'user_form':user_form,
        'transaction_form': transaction_formset,
        })
#function which add user,Use POST method. 
def add_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = UserForm()
        return render(request, 'Finance/index.html', {
            'form': form
        })



#function for shows user. Get users using method all(). 
# Use dictionary to set value, which will use later in template.
def show_users(request):
    users = User.objects.all()
    return render(request, 'Finance/show.html', {
        'user' : users
    })

def show_transaction(request):
    transaction = Transaction.objects.all()
    return render(request, 'Finance/show.html', {
        'transaction' : transaction
    })

#function for editing transactions. Use get metgod with argument id.
# Argument id is specific for every member of table. Commonly, that field is defined with primary key.
def edit_transaction(request):
    edit_trans = Transaction.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_transaction':edit_trans
    })


def edit_users(request):
    edit_user = User.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_users':edit_user
    })

#use function to delete objects specify by id.
def delete_transaction(request):
    del_trans = Transaction.objects.get(id = id)
    del_trans.delete()
    return redirect('Finance/show')


def delete_users(request):
    del_user = User.objects.get(id = id)
    del_user.delete()
    return redirect('Finance/show')

#function for view sum of income grouped by date
def SumofIncomeByDate(request):
    groupBy_date = Transaction.objects.values('date').annotate(Sum('amount'))
    return render(request, 'Finance/GroupBy.html', {
        'groupBy': groupBy_date
    })

#function for get payments filterin by date
def user_payments(request):
    u_paym = Transaction.objects.filter('date')
    return render(request, 'Finance/GroupBy.html', {
        'user_payments':u_paym
    })

#sorting transaction by date and amount
def sortingTransaction(request):
    sorting = Transaction.objects.all().order_by('date','amount')
    return render(request, 'Finance/GroupBy.html' , {
        'sorting':sorting
    })

