#!/usr/local/bin/python

from math import sqrt
from math import fabs
class fraction():
	def __init__(self, numerator = 1, denominator = 1):
		self.numerator = numerator  # Числитель
		self.denominator = denominator  # Знаменатель


	def printf(self):  # Выводит на экран дробь
		if self.numerator == 0 or self.denominator == 0:  # Если числитель или знаменатель равны нулю, то выводим нулевую дробь
			print(0)
		elif self.denominator < 0 and self.numerator < 0:
				if fabs(self.denominator == 1.0):  # Если знаменатель единица, то выводим целое число в форме float
					print(self.numerator)
				else:
					self.numerator *= -1  # Выводим положительную дробь 
					self.denominator *= -1
					print(f'{self.numerator}/{self.denominator}')
				
		elif self.denominator < 0 and self.numerator > 0:
			if fabs(self.denominator) == 1.0:
				print(-(fabs(self.numerator)))
				pass
			else:
			 # Выводим положительную дробь с минусом впереди
				self.denominator *= -1
				print(f'-{self.numerator}/{self.denominator}') 
				pass
			
		elif self.denominator > 0 and self.numerator < 0:
			if self.denominator == 1.0:
				print(-(fabs(self.numerator)))
				pass
			else:
				# Выводим положительную дробь с минусом впереди
				self.numerator *= -1   
				print(f'-{self.numerator}/{self.denominator}') 
				pass
			
		else:  
			# Выводим дробь, так как она положительная
			if fabs(self.denominator) == 1.0:
				print((fabs(self.numerator)))
				pass
			else:
				print(f'{self.numerator}/{self.denominator}')

 
	def simplify(self):  # Упрощает дробь
		if self.numerator == 0 or self.denominator == 0:
			result = fraction(0)
		elif self.numerator % self.denominator == 0:
			self.numerator /= self.denominator
			self.denominator /= self.denominator
		elif self.denominator % self.numerator == 0:
			self.denominator /= self.numerator
			self.numerator /= self.numerator
		for j in range(1,3):  # Запускаем несколько проверок, чтобы гарантировано упростить 
			for i in range(1, int(sqrt(fabs(self.numerator))) + 1):  #  Перебираем делители
				if self.denominator % i == 0 and self.numerator % i == 0:
					self.denominator /= i
					self.numerator /= i
		result = fraction(self.numerator, self.denominator)
		


	def summary(self, my_number):  # Сложение двух дробей (крест на крест)
		result_numerator = self.numerator*my_number.denominator + self.denominator*my_number.numerator
		result_denominator = self.denominator * my_number.denominator
		result = fraction(result_numerator, result_denominator)
		result.simplify()
		print("Sum result of 2 numbers equal:")
		result.printf()


	def multiply(self, my_number):  # Умножение двух дробей
		result_numerator = self.numerator*my_number.numerator
		result_denominator = self.denominator * my_number.denominator
		result = fraction(result_numerator, result_denominator)
		result.simplify()
		print("Multiply result of 2 numbers equal:")
		result.printf()


	def division(self, my_number):  # Деление двух дробей
		result_numerator = self.numerator*my_number.denominator
		result_denominator = self.denominator * my_number.numerator
		result = fraction(result_numerator, result_denominator)
		result.simplify()
		print("Division result of 2 numbers equal:")
		result.printf()
		# if result.denominator == 1.0:
		# 	print(result.numerator)


	def subtraction(self, my_number):  # Вычитание двух дробей (крест на крест)
		result_numerator = self.numerator * my_number.denominator - self.denominator * my_number.numerator
		result_denominator = self.denominator * my_number.denominator
		result = fraction(result_numerator, result_denominator)
		result.simplify()
		print("Substraction result of 2 numbers equal:")
		result.printf()


number1 = fraction(-115, 118)  # Создаем первую дробь
number2 = fraction(-73, 41)  # Создаем вторую дробь
number1.summary(number2)   # Вызываем все объявленные функции
number1.multiply(number2)
number1.subtraction(number2)
number1.division(number2)