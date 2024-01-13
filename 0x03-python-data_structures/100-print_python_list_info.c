#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "python.h"
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints some
 * basic info about Python lists
 * @p: A PyObject list
 *
 */
void print_python_list_info(PyObject *p)
{
	int r;

	printf("[*] Size of the Python List = %lu\n", Py_Size);
	printf("[*] Allocate = %lu\n", ((PyListObject *)p)->allocated);

	for (r = 0 ; r < Py_size(p) ; r++)
		printf("Element %d: %s\n", r, Py_Type(Pylist_GetItem(p, r))->tp_name);
}
