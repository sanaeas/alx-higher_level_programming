#include "lists.h"

/**
 * malloc_arr - allocate memory for array to store data
 *
 * @head: the head of the linked list
 *
 * Return: void
 */
int *malloc_arr(listint_t *head)
{
	int *arr,  length;

	length = 0;
	while (head)
	{
		length++;
		head = head->next;
	}

	arr = malloc(sizeof(int) * length);
	if (!arr)
		exit(1);
	return (arr);
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
	listint_t *temp;
	int i, *arr;

	if (!head || !(*head))
		return (1);

	arr = malloc_arr(*head);
	temp = *head;
	i = 0;
	while (temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}

	temp = *head, i -= 1;
	while (i >= 0)
	{
		if (arr[i] != temp->n)
		{
			free(arr);
			return(0);
		}
		temp = temp->next;
		i--;
	}
	free(arr);
	return (1);
}
