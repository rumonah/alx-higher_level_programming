#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 *is_palindrome - identify if a singly linked list is palindrome
 *@head: head of listint_t
 *Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *head1 = *head;
	listint_t *pal = NULL, *pal2 = NULL;

	if (*head == NULL || head1->next == NULL)
		return (1);
	while (head1 != NULL)
	{
		add_nodeint_end(&pal, head1->n);
		head1 = head1->next;
	}
	pal2 = pal;
	while (*head != NULL)
	{
		if ((*head)->n != pal2->n)
		{
			free_listint(pal);
			return (0);
		}
		*head = (*head)->next;
		pal2 = pal2->next;
	}
	free_listint(pal);
	return (1);
}


/**
 *add_nodeint - adds a new node at the beginning of a listint_t list
 *@head: head of listint_t
 *@n: int to add in listint_t list
 *Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
