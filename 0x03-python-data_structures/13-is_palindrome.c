#include "lists.h"

/**
 * is_palindrome - A function in C that checks if a
 *                 singly linked list is palindrome.
 * @head: a pointer to a pointer to the head node
 *
 * Return: 1 if palindrome or 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *rev_list;
	listint_t *current;
	listint_t *prev;
	listint_t *next;

	if (head == NULL || *head == NULL)
		return (1);
	rev_list = *head;
	prev = NULL;
	current = rev_list;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = rev_list;
		current = next;
	}
	rev_list = prev;

	current = *head;

	while (current != NULL)
	{
		if (current->n != rev_list->n)
			return (0);
		current = current->next;
		rev_list = rev_list->next;
	}

	return (1);
}
