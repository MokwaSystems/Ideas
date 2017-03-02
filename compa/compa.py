#!/usr/bin/python
#-*- coding: windows-1250 -*-

import os
import sys
import getopt

DEBUG = False
Difrence = []
counter_difrence = 0

# -h - pomoc; -n - nie bierz pod uwag� linii -l bierz pod uwag� lini�; -g <filename> generuj plik poprawiony z ogrygina�; -o --output-log logi

def print_help():
	print "..........:::::::::: COMPA - RER ::::::::::.........."
	print
	print u"Autor: Przemys�aw Mokwa"
	print u"Licencja: Open-source"
	print
	print u"Za pomoc� tego programu mo�esz por�wna� dwa pliki pod wzgl�dem zawarto�ci,"
	print u"znale�� te r�nice krok po kroku, lub wygenerwowa� plik z zmianami wzgl�dem orygina�u"
	print u"oraz plik z logami zmian. Celem programu jest u�yteczno�� i szybkie dzia�anie."
	print u"Po co? Poniewa� ten program jest Ci potrzebny gdy w ogromnym pliku kodu programu szukasz liter�wki,"
	print u"a nie masz dost�pu do swojego ulubionego �rodowiska"
	print
	print u"Wywo�anie programu: "
	print u"compo.py OPTIONS <filename_org> <filename_compare>"
	print u"Dost�pne opcje: "
	print u"compa.py -h , --help\t==> Wy�wietlenie pomocy"
	print u"compa.py -n , --no-line\t==> Program nie bierze pod uwag� numeracji linii. Por�wnuje tylko zawarto�� tekstu"
	print u"compa.py -l , --line-on\t==> Program bierze pod uwag� numeracje lini i opcja wchodzi w sk�adnik do por�wnania"
	print u"compa.py -g <filename> , --genere <filename>\t==> Program tworzy poprawiony plik wzgl�dem orygina�u"
	print u"compa.py -o <filename> , --output-log <filename>\t==> Utworzenie pliku z logami zmian"
	print u"compa.py -d , --debug\t==> W��cza dodatkowe informacje (zwi�zane z prac� programu, nie wykonywanymi zadaniami)"
	print 
	print u"Przyk�ady: "
	print 
	print u"Bez liczenia lini, generuj plik z logami:"
	print u"compa.py -n -o log.txt org.txt tocompare.txt"
	print
	print u"Z liczeniem lini, z generacj� poprawionego pliku, z generowaniem pliku z logami"
	print u"compa.py -l -g improve.txt -o log.txt org.txt tocompare.txt"
	print u"compa.py -g improve.txt -o log.txt org.txt tocompare.txt"
	print 
	print u"Zwyk�e wy�wietlenie r�nic (r�nica po r�nicy)"
	print u"compa.py org.txt tocompare.txt"
	print
	print "..........:::::::::: COMPA - RER ::::::::::.........."

def Compare( org_line, comp_line ):
	flag_equals_len_line = True
	global Difrence
	global counter_difrence
	
	len_org_line = len(org_line)
	len_comp_line = len(comp_line)
	
	if len_org_line != len_comp_line:
		print u"[ !!! ] R�nica w d�ugo�ci lini - co� si� nie zgadza\t\t...WARNING"
		flag_equals_len_line = False
	
	len_greater_line = len_org_line;
	if not flag_equals_len_line:
		if len_org_line > len_comp_line:
			len_greater_line = len_org_line
		elif len_comp_line > len_org_line:
			len_greater_line = len_org_line
			
	if DEBUG:
		print "len_greater_line = %i" % len_greater_line
		print "len_org_line = %i" % len_org_line
		print "len_comp_line = %i" % len_comp_line
		print "CHUJ!\n"
	# TUTAJ JEST CO� ZJEBANE
	for i in range(len_greater_line):
		if org_line[i] != comp_line[i]:
			print u"Znalaz�em %i r�nic�! Wyraz oryginalny: %s != %s :Wyraz por�wnawczy. Literka %s != %s" % ( i, "<bd>", "<bd>", org_line[i], comp_line[i])
			counter_difrence += 1
			Difrence.append(comp_line)
			
	return
			
def CompareTwo( org_line, comp_line ):
	flag_equals_len_line = True
	global Difrence
	global counter_difrence
	
	len_org_line = len(org_line)
	len_comp_line = len(comp_line)
	
	if len_org_line != len_comp_line:
		print u"[ !!! ] R�nica w d�ugo�ci lini - co� si� nie zgadza\t\t...WARNING"
		flag_equals_len_line = False
	
	len_greater_line = len_org_line;
	if not flag_equals_len_line:
		if len_org_line > len_comp_line:
			len_greater_line = len_org_line
		elif len_comp_line > len_org_line:
			len_greater_line = len_org_line
	if DEBUG:
		print "len_greater_line = %i" % len_greater_line
		print "len_org_line = %i" % len_org_line
		print "len_comp_line = %i" % len_comp_line
		print "CHUJ!\n"
	
	words_org = org_line.split()
	words_compa = comp_line.split()
	len_wrods_org = len(words_org)
	len_words_compa = len(words_compa)

	greater_len_words = GetGreater(len_wrods_org, len_words_compa)
	if len_wrods_org != greater_len_words:
		print "[ WARNING ] R�cnia w ilo�ci s��w!"
			
	# TUTAJ!
	return

def Summary():
	print u"Znalezionych r�nic: %i\n" % counter_difrence
	print u"Lista r�nic (wy�wietlane s� linie z pliku do por�wnania, nie z orygina�u!):\n"
	for i in range(len(Difrence)):
		print u"%i: %s" % (i, Difrence[i])
	print u"\nKoniec."
	
	
def OpenFile(fname):
	try:
		tempFile = open(fname, 'r' )
		print u"[   LOG ] OpenFile succesfuly opened!\t\t...OK\n"
		return tempFile
	except IOError as e:
		print u"OpenFile Function failed: %s\n" % e
		sys.exit()
		
def SaveFile(fname):
	try:
		tempFile = open(fname, 'w')
		print u"[   LOG ] SaveFile succesfuly opened!\t\t...OK\n"
		return tempFile
	except IOError as e:
		print u"SaveFile function failed: %s\n" % e
		sys.exit()
		
def CounterLines(file):
	count = -1
	for count, wiersz in enumerate(file):
		pass
	count += 1
	file.seek(0)
	return count
	
def GetGreater( a, b ):
	if a > b:
		if DEBUG:
			print "Wiekszy pierwszy paramter a: %i > %i" % (a, b)
		return a
	elif a < b:
		if DEBUG:
			print "Wiekszy pierwszy paramter b: %i < %i" % (a, b)
		return b
	elif a == b:
		if DEBUG:
			print "Parametry s� r�wne: %i == %i" % (a, b)
		return a

def GetSmaller( a, b ):
	if a > b:
		if DEBUG:
			print "Mniejszy drugi paramter b: %i > %i" % (a, b)
		return b
	elif a < b:
		if DEBUG:
			print "Mniejszy pierwszy paramter a: %i < %i" % (a, b)
		return a
	elif a == b:
		if DEBUG:
			print "Parametry s� r�wne: %i == %i" % (a, b)
		return a
	
def main(argv):
	global DEBUG

	fn_f = ""
	fn_s = ""
	fn_g = ""
	fn_l = "log.txt"
	
	try:
		opts, args = getopt.getopt(argv, "hnlg:o:d", ["help","no-line","line-on","genere=", "output-log=", "debug"] )
	except  getopt.GetoptError:
		print u"Fejjjlaaaa something was wrong in getopt function"
		sys.exit(2)
		
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			# Wy�wietl pomoc
			print_help()
			sys.exit()
		elif opt in ("-n", "--no-line"):
			# Flaga: nie bierz pod uwag� linii
			print u"Nie bior� pod uwag� numeracji linii\n"
			#sys.exit()
		elif opt in ("-l", "--line-on"):
			# Flaga bierz pod uwage lini�
			print u"Bior� pod uwag� numeracj� linii\n"
			#sys.exit()
		elif opt in ("-g", "--genere"):
			# Generuj plik wyj�ciowy
			fn_g = arg
			print u"Nazwa pliku do wygenerowania %s\n" % fn_g
			if fn_g == "":
				print u"Nie podano nazwy pliku dla wygenerowania poprawionego pliku\n"
				sys.exit()
		elif opt in ("-o", "--output-log"):
			# Generuj plik wyj�ciowy
			fn_l = arg
		elif opt in ("-d", "--debug"):
			# Generuj plik wyj�ciowy
			DEBUG = True
			print u"Tryb informacji debuguj�cych w��czony!\n"
	
	argv_len = len(argv) - 1
	if len(argv) > 1:
		if DEBUG:
			print u"Warto�� argv od 1: %s\n" % argv
		tempArg = argv[argv_len-1]
		if tempArg[0] != '-':
			fn_f = argv[argv_len-1]
			fn_s = argv[argv_len]
	else:
		print u"Nie podano argument�w!\n"
		print_help()
		sys.exit()
	
	if fn_f == "" or fn_s == "":
		print u"Nie podano nazw plik�w\n"
		sys.exit(2)
	
	if DEBUG:
		print u"[   LOG ] fn_f = %s : fn_s = %s : fn_g = %s : fn_l = %s\n" % (fn_f, fn_s, fn_g, fn_l)
	
	# Otwarcie plik�w "g��wnych" - wzorca i do por�wnania
	File_ORG = OpenFile(fn_f)
	File_COMP = OpenFile(fn_s)
	if DEBUG:
		print u"Otwarcie pliku sie powiod�o\n"
		
	try:
		num_line_org = CounterLines(File_ORG)
		num_line_comp = CounterLines(File_COMP)
		greater_line = 0
		
		if num_line_org != num_line_comp:
			print u"[ WARNING ] Liczba linii w plikach jest r�na!"
		
		if DEBUG:
			print u"NUM LINE ORG = %i" % num_line_org
			print u"NUM LINE COMP = %i" % num_line_comp
			
		greater_line = GetSmaller(num_line_org, num_line_comp)
		if DEBUG:
			print "Greater Line = %i" % greater_line
		
		#lines_original_file = File_ORG.readlines()
		#lines_compare_file = File_COMP.readlines()
		lines_original_file = []
		lines_compare_file = []
		for lineorg in File_ORG:
			lines_original_file.append(lineorg)
			
		
		for linecomp in File_COMP:
			lines_compare_file.append(linecomp)
		
		if DEBUG:
			print "______________________ ORG LINE: "
			print lines_original_file
			print
			print "______________________ COMPARE LINE: "
			print lines_compare_file
		
		for i in range(greater_line):
			print "==> %i" % i
			CompareTwo(lines_original_file[i], lines_compare_file[i])
		
	except ValueError as e:
		if DEBUG:
			print u"[   ERROR LOG ] Nie uda�o sie odczyat� z pliku: %s" % e
		
	Summary()
	File_ORG.close()
	File_COMP.close()
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	