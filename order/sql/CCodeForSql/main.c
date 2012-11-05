#include "stdio.h"
#include "math.h"
#include "string.h"

#define MAX_PROD 5
#define MAX_CUST 5
#define MAX_QTY 5
#define PAYMENT_MODES 3

#define MIN_ORDERS 2000

int main()
{
	FILE * fp1 = fopen("order.sql", "w");
	FILE * fp2 = fopen("orderitem.sql", "w");
	int i, j, k, random, prod, cust, orders, orderitems, count, pay, payment_realised, quantity, current_order, increment_order, increment_order_in_next_iteration=0;
	char str[10], quotes = '"';
	char payment[4];
	prod = rand()%MAX_PROD;

	printf("Give Number of orders:");
	scanf("%d", &orders);
	orders = MIN_ORDERS + orders%MIN_ORDERS;
	printf("Give Number of orderitems:");
	scanf("%d", &orderitems);
	orderitems = MIN_ORDERS*3 + orderitems%MIN_ORDERS;

	for (i=0, count=1; i<orders; i++, count++)
	{	
		cust = rand()%MAX_CUST+1;
		pay = rand()%PAYMENT_MODES;
		if (pay==0) strcpy(payment, "cc");
		else if (pay==1) strcpy(payment, "nb");
		else strcpy(payment, "cod");
		payment_realised = rand()%2;
		fprintf(fp1, "insert into order_order (customer_id, payment_method, amount, payment_realised, id) values");
		fprintf(fp1, "(%d, %c%s%c, 0, %d, %d);\n", cust, quotes, payment, quotes, payment_realised, count);
	}
	;
	for(i=0, count=0, current_order = 1; i<orderitems && current_order <= orders; i++, count++)
	{

		prod = rand()%MAX_PROD+1;
		quantity = rand()%MAX_QTY+1;
		fprintf(fp2, "insert into order_orderitem (id, quantity, product_id, order_id) values");
		fprintf(fp2, "(%d, %d, %d, %d);\n", count, quantity, prod, current_order);
		increment_order = rand()%2;
		if (increment_order == 0 || increment_order_in_next_iteration==0)
		{
			current_order++;
			increment_order_in_next_iteration =2;
		}
		else 
		{
			increment_order_in_next_iteration--;
		}
	}
	feof(fp1);
	feof(fp2);
	return 0;
}
