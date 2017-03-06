#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import getopt

DEBUG = False
Difrence = []
counter_difrence = 0
word = " <word> "
levelingline = " <levelingline> "

# -h - pomoc; -n - nie bierz pod uwagę linii -l bierz pod uwagę linię; -g <filename> generuj plik poprawiony z ogryginał; -o --output-log logi

def print_help():
	print "..........:::::::::: COMPA - RER ::::::::::.........."
	print
	print "Autor: Przemyslaw Mokwa"
	print "Licencja: Open-source"
	print
	print "Za pomoca tego programu mozesz porownac dwa pliki pod wzgledem zawartosci,"
	print "znalezc te roznice krok po kroku, lub wygenerwowac plik z zmianami względem oryginalu"
	print "oraz plik z logami zmian. Celem programu jest uzyteczność i szybkie dzialanie."
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
	global word
	global levelingline
	
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
	
	words_org = org_line.split()
	words_compa = comp_line.split()
	len_words_org = len(words_org)
	len_words_compa = len(words_compa)

	greater_len_words = GetGreater(len_words_org, len_words_compa)
	if len_words_org != len_words_compa:
		print "[ WARNING ] Rozcnia w ilosci slow!"
		if len_words_org < len_words_compa:
			for i in range( (len_words_compa - len_words_org) ):
				words_org.append(word)
				if DEBUG:
					print "Dodalem slowko w tablicy org"
		else:
			for i in range( (len_words_org - len_words_compa) ):
				words_compa.append(word)
				if DEBUG:
					print "Dodalem slowko w tablicy comp"
					
	# W tym miejscu jest prawdopodobny błąd logiczny!
	if words_org[0] == levelingline:
		counter_difrence += 1
		print "[ ROZNICA ] %i ==> LINIA Z PLIKU PROBKI NIE OBECNA W ORYGINALE W TYM MIEJSCU\t\t...WARNING" % (counter_difrence)
		Difrence.append( ("Roznica %i: LINIA Z PLIKU PROBKI NIE OBECNA W ORYGINALE W TYM MIEJSCU" % (counter_difrence) ) )
		if DEBUG:
			print "Sprawdzono wszystkie dane w wierszu - czekam na nastepny\t\t...OK"
		return
		
	if words_compa[0] == levelingline:
		counter_difrence += 1
		print "[ ROZNICA ] %i ==> LINIA Z ORYGINALNEGO PLIKU NIE OBECNA W PLIKU PROBCE W TYM MIEJSCU\t\t...WARNING" % (counter_difrence)
		Difrence.append( ("Roznica %i: LINIA Z ORYGINALNEGO PLIKU NIE OBECNA W PLIKU PROBCE W TYM MIEJSCU" % (counter_difrence) ) )
		if DEBUG:
			print "Sprawdzono wszystkie dane w wierszu - czekam na nastepny\t\t...OK"
		return
			

	for i in range(greater_len_words):
		if words_org[i] != words_compa[i]: # Ziomek - coś się nie zgadza
			print "%i Cos mi sie nie zgadza..." % (i)
			if ( i + 1 ) < greater_len_words: # Sprawdz mi licznik
				print "%i Licznik o jeden wiecej nie wykracza" % (i)
				if words_org[ i + 1 ] != "": # Sprawdz czy kolejne słowo oryginału nie jest puste
					print "%i Kolejne slowo oryginalu NIE jest puste" % (i)
					if words_compa[i] == words_org[ i + 1 ]: # Sprawdz aktualne słowo próbki (plik porównawczy) z kolejnym słowem oryginału
						temp_idx = i
						temp_j = 0
						counter_difrence += 1
						temp_words_compa = []
						print "[ ROZNICA ] %i ==> oryginal: %s vs. BRAK_SLOWA :porownawczy\t\t...WARNING" % (counter_difrence, words_org[i])
						Difrence.append( ("Roznica %i: %s vs. BRAK SLOWA" % (counter_difrence, words_org[i]) ) )
						# ----- <words> z konca lini przesunac w miejsce gdzie jest BRAK_SLOWA ------
						# Program musi się dowiedzieć która linia jest ta dłuższa czy originalna czy probka
						if words_compa[greater_len_words - 1] == word: # Jeśli próbka ma na końcu lini dodane słowo <word>
							words_compa.pop() # Usuń ostatni
							for j in range(temp_idx): # skopiuj do tymczasowej tablicy pierwszą część tablicy z słowami
								temp_words_compa.append(words_compa[j])
								temp_j += 1
							if DEBUG:
								print "[ LOG 1 ] temp_words_compa == %s" % temp_words_compa
							temp_words_compa.append(word) # Dodaj słówko <word> w miejsce gdzie jest brak słowa
							if DEBUG:
								print "[ LOG 2 ] temp_words_compa == \t%s : \t\ttemp_j == %i" % (temp_words_compa, temp_j)
								print "[ LOG 2 ] words_compa == \t%s : \t\ttemp_j == %i" % (words_compa, temp_j)
							for j in range(temp_j, greater_len_words-1): # skopiuj dalszą część tablicy począwszy od następnego słowa po wychwyconym błędzie
								print "======> %i " % j
								temp_words_compa.append(words_compa[j])	
							if DEBUG:
								print "[ LOG 3 ] temp_words_compa == %s" % temp_words_compa
							words_compa = temp_words_compa # Do głównej tablicy z słowami przypisz tymczasową po zmianach
							if DEBUG:
								print "[ LOG 4 ] words_compa == %s \nKONIEC!" % words_compa	
					elif words_org[i] == words_compa[i + 1]:
						temp_idx = i
						temp_j = 0
						counter_difrence += 1
						temp_words_org = []
						print "[ ROZNICA ] %i ==> oryginal: %s vs. BRAK_SLOWA :porownawczy\t\t...WARNING" % (counter_difrence, words_org[i])
						Difrence.append( ("Roznica %i: %s vs. BRAK SLOWA" % (counter_difrence, words_org[i]) ) )
						# ----- <words> z konca lini przesunac w miejsce gdzie jest BRAK_SLOWA ------
						# Program musi się dowiedzieć która linia jest ta dłuższa czy originalna czy probka
						if words_org[greater_len_words - 1] == word:
							words_org.pop() # Usuń ostatni
							for j in range(temp_idx): # skopiuj do tymczasowej tablicy pierwszą część tablicy z słowami
								temp_words_org.append(words_org[j])
								temp_j += 1
							if DEBUG:
								print "[ LOG 1 ] temp_words_org == %s" % temp_words_org
							temp_words_org.append(word) # Dodaj słówko <word> w miejsce gdzie jest brak słowa
							if DEBUG:
								print "[ LOG 2 ] temp_words_org == \t%s : \t\ttemp_j == %i" % (temp_words_org, temp_j)
								print "[ LOG 2 ] words_org == \t%s : \t\ttemp_j == %i" % (words_org, temp_j)
							for j in range(temp_j, greater_len_words-1): # skopiuj dalszą część tablicy począwszy od następnego słowa po wychwyconym błędzie
								print "======> %i " % j
								temp_words_org.append(words_org[j])	
							if DEBUG:
								print "[ LOG 3 ] temp_words_org == %s" % temp_words_org
							words_org = temp_words_org # Do głównej tablicy z słowami przypisz tymczasową po zmianach
							if DEBUG:
								print "[ LOG 4 ] words_compa == %s \nKONIEC!" % words_org
					#elif words_compa[i] != words_org[ i + 1 ] or words_org[i] != words_compa[i + 1]:
					else:
						counter_difrence += 1
						print "[ ROZNICA ] %i ==> oryginal: %s vs. %s :porownawczy\t\t...WARNING" % (counter_difrence, words_org[i], words_compa[i])
						Difrence.append( ("Roznica %i: %s vs. %s" % (counter_difrence, words_org[i], words_compa[i]) ) )
				else:
					counter_difrence += 1
					print "[ ROZNICA ] %i ==> oryginal: %s vs. %s :porownawczy\t\t...WARNING" % (counter_difrence, words_org[i], words_compa[i])
					Difrence.append( ("Roznica %i: %s vs. %s" % (counter_difrence, words_org[i], words_compa[i]) ) )
			else:
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
	global levelingline
	
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
			# Wyświetl pomoc
			print_help()
			sys.exit()
		elif opt in ("-n", "--no-line"):
			# Flaga: nie bierz pod uwagę linii
			print "Nie biore pod uwage numeracji linii\n"
			#sys.exit()
		elif opt in ("-l", "--line-on"):
			# Flaga bierz pod uwage linię
			print "Biore pod uwage numeracje linii\n"
			#sys.exit()
		elif opt in ("-g", "--genere"):
			# Generuj plik wyjściowy
			fn_g = arg
			print "Nazwa pliku do wygenerowania %s\n" % fn_g
			if fn_g == "":
				print "Nie podano nazwy pliku dla wygenerowania poprawionego pliku\n"
				sys.exit()
		elif opt in ("-o", "--output-log"):
			# Generuj plik wyjściowy
			fn_l = arg
		elif opt in ("-d", "--debug"):
			# Generuj plik wyjściowy
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
	
	# Otwarcie plików "głównych" - wzorca i do porównania
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
		temp_lines_compare_file = []
				
		for linecomp in File_COMP:
			temp_lines_compare_file.append(linecomp.strip())
			
		lines_compare_file = []
		for lineorg in File_ORG:
			lines_original_file.append(lineorg.strip())
			if(lineorg.strip()  )
		#for i in range(len(lines_original_file)):
			
			
		# Jeśli w oryginalnym pliku będzie więcej linii niż w próbce oznacza to, że próbka ma tych linii za mało (serio?) czyli dodajemy <levelingline>
			
		#if flag_not_equals_line:
		#	if num_line_org < num_line_comp:
		#		lines_original_file.append(levelingline)
		#		if DEBUG:
		#			print "Znalazlem pusta linie w ORIGINAL file - dodalem %s" % levelingline
		#	if num_line_comp < num_line_org:
		#		lines_compare_file.append(levelingline)
		#		if DEBUG:
		#			print "Znalazlem pusta linie w COMPA file - dodalem %s" % levelingline		
		if DEBUG:
			print "______________________ ORG LINE: "
			print lines_original_file
			print
			print "______________________ COMPARE LINE: "
			print lines_compare_file
		
		for i in range(greater_line):
			print "==> %i" % i
			Compare(lines_original_file[i], lines_compare_file[i])
		
	except ValueError as e:
		if DEBUG:
			print "[   ERROR LOG ] Nie udalo sie odczyatc z pliku: %s" % e
		
	Summary()
	File_ORG.close()
	File_COMP.close()
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	