#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * is_palindrome - A function that checks if a list is a palindrome.
 * @head: The pointer to the head of the list.
 * Return: 0 if list not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int len_nodes = 0, i = 0, *array = NULL;

    if (*head == NULL || head == NULL || (*head)->next == NULL)
        return (1);
    while (temp)
    {
        len_nodes++;
        temp = temp->next;
    }
    array = malloc(len_nodes * sizeof(int));
    temp = *head;
    while (temp)
    {
        array[i++] = temp->n;
        temp = temp->next;
    }
    for (i = 0; i < len_nodes / 2; i++)
    {
        if (array[i] != array[len_nodes - 1 - i])
        {
            free(array);
            return (0);
        }
    }
    free(array);
    return (1);
}
