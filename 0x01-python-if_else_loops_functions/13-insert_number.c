#include "lists.h"

/**
 * insert_node - a function that inserts a node to a sorted list
 *
 * @head: a pointer to the pointer of the head node
 * @number: the data for the new node
 * Return: The new noe
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *prev;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->next = NULL;
	newnode->n = number;

	if (head == NULL || *head == NULL)
	{
		newnode->next = *head;
		*head = newnode;

		return (newnode);
	}

	current = *head;
	while (current != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}
	prev->next = newnode;
	newnode->next = current;

	return (newnode);
}
