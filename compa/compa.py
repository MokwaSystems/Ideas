#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import getopt

DEBUG = False
Difrence = []
counter_difrence = 0

# -h - pomoc; -n - nie bierz pod uwagê linii -l bierz pod uwagê liniê; -g <filename> generuj plik poprawiony z ogrygina³; -o --output-log logi

def print_help():
	print "..........:::::::::: COMPA - RER ::::::::::.........."
	print
	print "Autor: Przemyslaw Mokwa"
	print "Licencja: Open-source"
	print
	print "Za pomoca tego programu mozesz porownac dwa pliki pod wzgledem zawartosci,"
	print "znalezc te roznice krok po kroku, lub wygenerwowac plik z zmianami wzglêdem oryginalu"
	print "oraz plik z logami zmian. Celem programu jest uzytecznoœæ i szybkie dzialanie."
	print "Po co? Poniewaz ten program jest Ci potrzebny gdy w ogromnym pliku kodu programu szukasz literowki,"
	print "a nie masz dostepu do swojego ulubionego srodowiska"
	print
	print "Wywolanie programu: "
	print "compo.py OPTIONS <filename_org> <filename_compare>"
	print "Dostepne opcje: "
	print "compa.py -h , --help\t==> Wyswietlenie pomocy"
	print "compa.py -n , --no-line\t==> Program nie bierze pod uwage numeracji linii. Porownuje tylko zawartosc tekstu"
	print "compa.py -l , --line-on\t==> Program bierze pod uwage numeracje linii i opcja wchodzi w skladnik do porownania"
	print "compa.py -g <filename> , --genere <filename>\t==> Program tworzy poprawiony plik wzgledem oryginalu"
	print "compa.py -o <filename> , --output-log <filename>\t==> Utworzenie pliku z logami zmian"
	print "compa.py -d , --debug\t==> Wlacza dodatkowe informacje (zwiazane z praca programu, nie wykonywanymi zadaniami)"
	print 
	print "Przyklady: "
	print 
	print "Bez liczenia lini, generuj plik z logami:"
	print "compa.py -n -o log.txt org.txt tocompare.txt"
	print
	print "Z liczeniem lini, z generacja poprawionego pliku, z generowaniem pliku z logami"
	print "compa.py -l -g improve.txt -o log.txt org.txt tocompare.txt"
	print "compa.py -g improve.txt -o log.txt org.txt tocompare.txt"
	print 
	print "Zwykle wyswietlenie roznic (roznica po roznicy)"
	print "compa.py org.txt tocompare.txt"
	print
	print "..........:::::::::: COMPA - RER ::::::::::.........."

def Compare( org_line, comp_line ):
	flag_equals_len_line = True
	global Difrence
	global counter_difrence
	
	len_org_line = len(org_line)
	len_comp_line = len(comp_line)
	
	if len_org_line != len_comp_line:
		print "[ !!! ] Roznica w dlugosci linii - cos sie nie zgadza\t\t...WARNING"
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
	# TUTAJ JEST COŒ ZJEBANE
	for i in range(len_greater_line):
		if org_line[i] != comp_line[i]:
			print "Znalazlem %i roznice! Wyraz oryginalny: %s != %s :Wyraz porownawczy. Literka %s != %s" % ( i, "<bd>", "<bd>", org_line[i], comp_line[i])
			counter_difrence += 1
			Difrence.append(comp_line)
			
	return
			
def CompareTwo( org_line, comp_line ):
	flag_equals_len_line = True
	global Difrence
	global counter_difrence
	
	#len_org_line = len(org_line)
	#len_comp_line = len(comp_line)
	
	#if len_org_line != len_comp_line:
	#	print "[ !!! ] Roznica w dlugosci lini - cos sie nie zgadza\t\t...WARNING"
	#	flag_equals_len_line = False
	
	#len_greater_line = len_org_line;
	#if not flag_equals_len_line:
	#	if len_org_line > len_comp_line:
	#		len_greater_line = len_org_line
	#	elif len_comp_line > len_org_line:
	#		len_greater_line = len_org_line

	#if DEBUG:
	#	print "len_greater_line = %i" % len_greater_line
	#	print "len_org_line = %i" % len_org_line
	#	print "len_comp_line = %i" % len_comp_line
	#	print "CHUJ!\n"
	
	words_org = org_line.split()
	words_compa = comp_line.split()
	len_words_org = len(words_org)
	len_words_compa = len(words_compa)

	greater_len_words = GetGreater(len_words_org, len_words_compa)
	if len_words_org != len_words_compa:
		print "[ WARNING ] Rozcnia w ilosci slow!"
		if len_words_org < len_words_compa:
			for i in range( (len_words_compa - len_words_org) ):
				words_org.append(" <org>")
				if DEBUG:
					print "Dodalem slowko w tablicy org"
		else:
			for i in range( (len_words_org - len_words_compa) ):
				words_compa.append(" <compa>")
				if DEBUG:
					print "Dodalem slowko w tablicy comp"
			

	for i in range(greater_len_words):
		if words_compa[i] != words_org[i]:
			counter_difrence += 1
			print "[ ROZNICA ] %i ==> oryginal: %s vs. %s :porownawczy\t\t...WARNING" % (counter_difrence, words_org[i], words_compa[i])
			Difrence.append( ("Roznica %i: %s vs. %s" % (counter_difrence, words_org[i], words_compa[i]) ) )
		
	if DEBUG:
		print "Sprawdzono wszystkie dane w wierszu - czekam na nastepny\t\t...OK"
	return

def Summary():
	print "Znalezionych roznic: %i\n" % counter_difrence
	print "Lista roznic (wyswietlane sa linie z pliku do porownania, nie z oryginalu!):\n"
	for i in range(len(Difrence)):
		print "%i: %s" % (i, Difrence[i])
	print "\nKoniec."
	
	
def OpenFile(fname):
	try:
		tempFile = open(fname, 'r' )
		print "[   LOG ] OpenFile succesfuly opened!\t\t...OK\n"
		return tempFile
	except IOError as e:
		print "OpenFile Function failed: %s\n" % e
		sys.exit()
		
def SaveFile(fname):
	try:
		tempFile = open(fname, 'w')
		print "[   LOG ] SaveFile succesfuly opened!\t\t...OK\n"
		return tempFile
	except IOError as e:
		print "SaveFile function failed: %s\n" % e
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
			print "Parametry sa rowne: %i == %i" % (a, b)
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
			print "Parametry sa rowne: %i == %i" % (a, b)
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
		print "Fejjjlaaaa something was wrong in getopt function"
		sys.exit(2)
		
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			# Wyœwietl pomoc
			print_help()
			sys.exit()
		elif opt in ("-n", "--no-line"):
			# Flaga: nie bierz pod uwagê linii
			print "Nie biore pod uwage numeracji linii\n"
			#sys.exit()
		elif opt in ("-l", "--line-on"):
			# Flaga bierz pod uwage liniê
			print "Biore pod uwage numeracje linii\n"
			#sys.exit()
		elif opt in ("-g", "--genere"):
			# Generuj plik wyjœciowy
			fn_g = arg
			print "Nazwa pliku do wygenerowania %s\n" % fn_g
			if fn_g == "":
				print "Nie podano nazwy pliku dla wygenerowania poprawionego pliku\n"
				sys.exit()
		elif opt in ("-o", "--output-log"):
			# Generuj plik wyjœciowy
			fn_l = arg
		elif opt in ("-d", "--debug"):
			# Generuj plik wyjœciowy
			DEBUG = True
			print "Tryb informacji debugujacych wlaczony!\n"
	
	argv_len = len(argv) - 1
	if len(argv) > 1:
		if DEBUG:
			print "Wartosc argv od 1: %s\n" % argv
		tempArg = argv[argv_len-1]
		if tempArg[0] != '-':
			fn_f = argv[argv_len-1]
			fn_s = argv[argv_len]
	else:
		print "Nie podano argumentow!\n"
		print_help()
		sys.exit()
	
	if fn_f == "" or fn_s == "":
		print "Nie podano nazw plikow\n"
		sys.exit(2)
	
	if DEBUG:
		print "[   LOG ] fn_f = %s : fn_s = %s : fn_g = %s : fn_l = %s\n" % (fn_f, fn_s, fn_g, fn_l)
	
	# Otwarcie plików "g³ównych" - wzorca i do porównania
	File_ORG = OpenFile(fn_f)
	File_COMP = OpenFile(fn_s)
	if DEBUG:
		print "Otwarcie pliku sie powiodlo\n"
		
	try:
		num_line_org = CounterLines(File_ORG)
		num_line_comp = CounterLines(File_COMP)
		greater_line = 0
		flag_not_equals_line = False
		
		if num_line_org != num_line_comp:
			print "[ WARNING ] Liczba linii w plikach jest rozna!"
			flag_not_equals_line = True
		
		if DEBUG:
			print "NUM LINE ORG = %i" % num_line_org
			print "NUM LINE COMP = %i" % num_line_comp
			
		greater_line = GetGreater(num_line_org, num_line_comp)
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
			
		if flag_not_equals_line:
			if num_line_org < num_line_comp:
				lines_original_file.append("<levelingline>")
			if num_line_comp < num_line_org:
				lines_compare_file.append("<levelingline>")
		
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
			print "[   ERROR LOG ] Nie udalo sie odczyatc z pliku: %s" % e
		
	Summary()
	File_ORG.close()
	File_COMP.close()
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	