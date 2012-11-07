alias used
    alias pyc='find . -iname "*.pyc" -exec rm "{}" ";"'
        removes all cached pyc files

-> only search by order, product made functional
-> initial database values stored in 
        produxt/fixtures/
        customer/fixtures/
        #order/sql/  #generated using a C code in order/sql/CCodeForSql
        order/fixtures/

To run:

    -> install django v1.4
    -> copy src code/clone the repo
    -> to sync database, go to project root folder
            $$) python manage.py syncdb
                this will ask to create a superuser account, do create it.
       run server as
            $$) python manage.py runserver <<port number -- this port number is optional, default 8000>>
    
    ->  If you want to use random orders(in large nymbers, via script)
            compile C script in order/sql/CCodeForSql/
            run it
            move the generated files in order/sql/
        remove fixtures file from order/fixtures/
        sync database
        next, correct database orders entries 
            go to root folder for project
            $$) python manage.py shell
            $$) from order.models import Order
            $$) orders = Order.objects.all()
            $$) for o in orders:
                .... o.save()
