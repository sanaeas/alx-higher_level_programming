#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t size, i;

	size = Py_SIZE(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	i = 0;
	while (i < size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
