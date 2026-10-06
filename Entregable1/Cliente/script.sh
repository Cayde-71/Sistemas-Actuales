#!/bin/sh
{
    printf '%s\n' '+ 9 22'
    printf '%s\n' '- 30 15'
    printf '%s\n' '* 7 8'
    printf '%s\n' '/ 10 2'
    printf '%s\n' '^ 2 3'
    printf '%s\n' 'm 7 5'
} | nc -N mi_servidor 5088