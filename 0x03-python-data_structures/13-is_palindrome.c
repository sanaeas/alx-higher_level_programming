#include "lists.h"

/**
 * listToArray - Converts a linked list into array of data
 *
 * @head: the head of the linked list
 * @array: array to store data
 * @size: the length of the linked list
 *
 * Return: void
 */
void listToArray(listint_t *head, int *array, int size)
{
	int i = 0;
	listint_t *temp = head;

	while (temp != NULL && i < size)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: The head of the linked list
 *
 * Return: 0 not a palindrome | 1 is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0, *arr, i = 0, mid;
	const listint_t *temp = *head;

	if (!head || !(*head))
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	listToArray(*head, arr, len);
	mid = len / 2;
	len -= 1;
	for (i = 0; i < mid; i++)
	{
		if (arr[i] != arr[len])
		{
			free(arr);
			return (0);
		}
		len--;
	}
	free(arr);
	return (1);
}
