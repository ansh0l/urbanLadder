alias used
    alias pyc='find . -iname "*.pyc" -exec rm "{}" ";"'
        removes all cached pyc files

-> only search by order, product made functional
-> initial database values stored in 
        produxt/fixtures/
        customer/fixtures/
        order/sql/  #generated using a C code in order/sql/CCodeForSql

-> to start database
        $$) python manage.py syncdb
   next, correct database orders entries
        $$) python manage.py shell
        $$) from order.models import Order
        $$) orders = Order.objects.all()
        $$) for o in orders:
            .... o.save()
   run server as
        $$) python manage.py runserver
