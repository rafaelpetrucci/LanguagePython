from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(requests):
    return HttpResponse('<h1>Hello World</h1>')


def soma(requests, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>Hello, {} + {} = {}</h1>'.format(num1, num2, soma))


def subtracao(requests, num1, num2):
    sub = num1 - num2
    return HttpResponse('<h1>A subtração do número {} - {} = {}.'.format(num1, num2, sub))


def multiplicacao(requests, num1, num2):
    multi = num1 * num2
    return HttpResponse('<h1>A multiplicação de {} X {} = {}'.format(num1, num2, multi))


def division(requests, num1, num2):
    divisao = num1 / num2
    return HttpResponse('<h1>A Divisao de {} / {} = {:.2f}'.format(num1, num2,divisao))