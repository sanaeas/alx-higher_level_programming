#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: The head of the linked list
 *
 * Return: 0 not a palindrome | 1 is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *temp;

	if (!head || !(*head))
		return (1);

	slow = *head, fast = *head;
	prev = NULL, temp = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
