#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "python.h"
#include "object.h"
#include "listobject.h"

/**
 * print_python_list_info - function that prints some
 * basic info about Python lists
 * @p: A PyObject list
 *
 */
void print_python_list_info(PyObject *p)
{
	int r;

	printf("[*] Size of the Python List = %li\n", Py_Size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (r = 0 ; r < Py_size(p) ; r++)
		printf("Element %i: %s\n", r, Py_Type(Pylist_GetItem(p, r))->tp_name);
}
