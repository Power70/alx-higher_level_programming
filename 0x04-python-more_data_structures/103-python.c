#include <Python.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));

    if (PyBytes_Check(p)) {
        printf("  trying string: %s\n", PyBytes_AsString(p));

        printf("  first 10 bytes: ");
        size_t i;
        for (i = 0; i < (size_t)PyBytes_Size(p) && i < 10; ++i) {
            printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (PyBytes_Check(PyList_GetItem(p, i))) {
            print_python_bytes(PyList_GetItem(p, i));
        }
    }
}

