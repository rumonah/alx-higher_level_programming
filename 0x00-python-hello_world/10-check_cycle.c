#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *first = list;

	if (!list)
		return (0);

	while (current && first && first->next)
	{
		current = current->next;
		first = first->next->next;
		if (current == first)
			return (1);
	}

	return (0);
}
