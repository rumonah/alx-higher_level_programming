#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *start;

	start = malloc(sizeof(listint_t));
	if (start == NULL)
		return (NULL);
	start->n = number;

	if (node == NULL || node->n >= number)
	{
		start->next = node;
		*head = start;
		return (start);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	start->next = node->next;
	node->next = start;

	return (start);
}
