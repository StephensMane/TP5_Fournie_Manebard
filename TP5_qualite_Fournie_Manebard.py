# // feature 1 //

# test

def test_f1():
  assert Feature1("bob") == "Hello, Bob"
  assert Feature1("Bob") == "Hello, Bob"

# fonction

def Feature1(nom):

  if not nom[0].isupper():
    nom = nom[0:1].capitalize() + nom[1:]
    return("Hello, "+ nom)

  else:
    return("Hello, "+ nom)

# // feature 2 //

# test

def test_f2():

  assert Feature2(' ') == "Hello, my friend"

# fonction

def Feature2(nom):

  if nom.isspace():
    return("Hello, my friend")

# // feature 3 //

# test

def test_f3():

  assert Feature3("JERRY") == "HELLO, JERRY"

# fonction

def Feature3(nom):

  if nom.isupper():
    return("HELLO, "+ nom)

# // feature 4 //

# test

def test_f4x5():

  assert Feature4x5("Amy,bob") == "Hello, Amy Bob "

# fonction

def Feature4x5(nom):

  liste_noms = list()
  i = 0

  while i < len(nom):

    liste_noms += [""]
    while i < len(nom) and nom[i] != ',':

      liste_noms[len(liste_noms)-1] += nom[i]
      i += 1

    i += 1

  message = "Hello, "

  for noms in liste_noms:

    if not noms[0].isupper():
      noms = noms[0:1].capitalize() + noms[1:]

    message += noms +' '

  return message

# // feature 6 //

# test

def test_f6():
  assert Feature6("Amy,BOB,Jerry") == "Hello, Amy, Jerry. AND BOB !"

# fonction

def Feature6(nom):

  liste_noms = list()
  liste_min = list()
  liste_maj = list()
  i = 0

  while i < len(nom):

    liste_noms += [""]
    while i < len(nom) and nom[i] != ',':

      liste_noms[len(liste_noms)-1] += nom[i]
      i += 1

    i += 1

  for noms in liste_noms:

    if noms.isupper():
      liste_maj.append(noms)

    else :
      liste_min.append(noms)

  Message = "Hello, "

  for noms in liste_min:

    Message += noms

    if liste_min.index(noms) < len(liste_min)-1:

      Message +=', '

  Message +=". AND "

  for noms in liste_maj:

    Message += noms

    if liste_maj.index(noms) < len(liste_maj)-1:

      Message +=', '

  Message += " !"

  return Message


# // feature 7 //

# test

def test_f7():
  assert Feature7("bob,amy,jerry") == "Hello, Bob, Amy and Jerry"

# fonction

def Feature7(nom):

  liste_noms = list()

  i = 0

  while i < len(nom):

    liste_noms += ['']
    while i < len(nom) and nom[i] !=',':

      liste_noms[len(liste_noms)-1] += nom[i]
      i += 1

    i += 1

  Message = "Hello, "

  i=0

  for noms in liste_noms:

    if not noms[0].isupper():
      noms = noms[0:1].capitalize() + noms[1:]
      liste_noms[i]=noms

    Message += noms

    if liste_noms.index(noms) < len(liste_noms)-2:

      Message +=', '

    if liste_noms.index(noms) == len(liste_noms)-2:

      Message +=' and '

    i+= 1

  return Message


# // feature 8 //

# test

def test_f8():
  assert Feature8("Bob,  amy") == "Hello, Bob and Amy"

# fonction

def Feature8(nom):

  liste_noms = list()

  i = 0

  while i < len(nom):

    liste_noms += ['']
    while i < len(nom) and nom[i] !=',':

      if nom[i]==' ':
        i +=1
      else:
        liste_noms[len(liste_noms)-1] += nom[i]
        i += 1

    i += 1

  Message = "Hello, "

  i=0

  for noms in liste_noms:

    if not noms[0].isupper():
      noms = noms[0:1].capitalize() + noms[1:]
      liste_noms[i]=noms

    Message += noms

    if liste_noms.index(noms) < len(liste_noms)-2:

      Message +=', '

    if liste_noms.index(noms) == len(liste_noms)-2:

      Message +=' and '

    i+= 1

  return Message


# // feature 9 //

# test

def test_f9():

  assert Feature9("bob, !bob, amy, bob, !jerry, David") == "Hello, Amy and David"

# fonction

def Feature9(nom):

  liste_noms = list()
  liste_ignores = list()

  i = 0

  while i < len(nom):

    liste_noms += ['']
    while i < len(nom) and nom[i] !=',':

      if nom[i]==' ':
        i +=1
      else:
        liste_noms[len(liste_noms)-1] += nom[i]
        i += 1

    i += 1


  for n in liste_noms:

    if n[0] == '!':
      liste_ignores.append(n[1:])

  y=0

  while y < len(liste_noms):
    if liste_noms[y] in liste_ignores or liste_noms[y][0] == '!':
      liste_noms.remove(liste_noms[y])
    else:
      y+= 1

  Message = "Hello, "

  i=0

  for noms in liste_noms:

    if not noms[0].isupper():
      noms = noms[0:1].capitalize() + noms[1:]
      liste_noms[i]=noms

    Message += noms

    if liste_noms.index(noms) < len(liste_noms)-2:

      Message +=', '

    if liste_noms.index(noms) == len(liste_noms)-2:

      Message +=' and '

    i+= 1

  return Message


# // feature 10 //

# test

def test_f10():

  assert Feature10("bob, amy, bob, !jerry, jerry") == "Hello, Bob (x2), and Amy"

# fonctions

def Feature10(nom):

  liste_noms = list()
  liste_ignores = list()
  liste_evolue = list()

  i = 0

  while i < len(nom):

    liste_noms += ['']
    while i < len(nom) and nom[i] !=',':

      if nom[i]==' ':
        i +=1
      else:
        liste_noms[len(liste_noms)-1] += nom[i]
        i += 1

    i += 1


  for n in liste_noms:

    if n[0] == '!':
      liste_ignores.append(n[1:])

  y=0

  while y < len(liste_noms):
    if liste_noms[y] in liste_ignores or liste_noms[y][0] == '!':
      liste_noms.remove(liste_noms[y])
    else:
      y+= 1

  for e in liste_noms:
    if not e in liste_evolue:
      liste_evolue.append(e)
      liste_evolue.append(liste_noms.count(e))

  Message = "Hello, "

  i=0

  while i < len(liste_evolue):

    if not liste_evolue[i][0].isupper():
      noms = liste_evolue[i][0:1].capitalize() + liste_evolue[i][1:]
      liste_evolue[i]=noms

    Message += liste_evolue[i]

    if liste_evolue[i+1] > 1:

      Message +=' (x'+ str(liste_evolue[i+1]) +')'

      if i+1 == len(liste_evolue)-3:

        Message +=','

    if i+1 < len(liste_evolue)-3:

      Message +=', '

    if i+1 == len(liste_evolue)-3:

      Message +=' and '

    i+= 2

  return Message

# // feature 11//

# test

def test_f11():

  assert Feature11("bob, amy, bob, !jerry, jerry, Greg, Sophie, Rick,  Morty, Alonzo") == "Hello, world !"

def test_sous_1_f11():

  assert sous_1_Feature11("bob, amy, bob, !jerry, jerry, Greg, Sophie, Rick,  Morty, Alonzo") == ["Bob", 2, "Amy", 1, "Greg", 1, "Sophie", 1, "Rick", 1, "Morty", 1, "Alonzo", 1]

def test_sous_2_f11():

  assert sous_2_Feature11("bob, amy, bob, !jerry, jerry") == "Hello, Bob (x2), and Amy"

# sous fonction 1

def sous_1_Feature11(nom):

  liste_noms = list()
  liste_ignores = list()
  liste_evolue = list()

  i = 0

  while i < len(nom):

    liste_noms += ['']
    while i < len(nom) and nom[i] !=',':

      if nom[i]==' ':
        i +=1
      else:
        liste_noms[len(liste_noms)-1] += nom[i]
        i += 1

    i += 1


  for n in liste_noms:

    if n[0] == '!':
      liste_ignores.append(n[1:])

  y=0

  while y < len(liste_noms):
    if liste_noms[y] in liste_ignores or liste_noms[y][0] == '!':
      liste_noms.remove(liste_noms[y])
    else:
      y+= 1

  for e in liste_noms:
    if not e in liste_evolue:
      liste_evolue.append(e)
      liste_evolue.append(liste_noms.count(e))

  i=0

  while i < len(liste_evolue):

    if not liste_evolue[i][0].isupper():
      noms = liste_evolue[i][0:1].capitalize() + liste_evolue[i][1:]
      liste_evolue[i]=noms

    i+=2

  return liste_evolue

# sous fonction 2

def sous_2_Feature11(liste_evolue):

  Message = "Hello, "

  i=0

  while i < len(liste_evolue):

    Message += liste_evolue[i]

    if liste_evolue[i+1] > 1:

      Message +=' (x'+ str(liste_evolue[i+1]) +')'

      if i+1 == len(liste_evolue)-3:

        Message +=','

    if i+1 < len(liste_evolue)-3:

      Message +=', '

    if i+1 == len(liste_evolue)-3:

      Message +=' and '

    i+= 2

  return Message

# fonction

def Feature11(nom):

  liste_evolue = sous_1_Feature11(nom)

  if len(liste_evolue) > 10:
    return("Hello, world !")

  else:
    return sous_1_Feature11(liste_evolue)

# // feature 12//

# test

def test_f12():

  assert Feature12("BOB, AMY, BOB, !jerry, jerry, GREG, SOPHIE, Rick,  MORTY, ALONZO") == "HELLO, WORLD !"

# fonction

def Feature12(nom):

  liste_evolue = sous_1_Feature11(nom)

  maj=0
  i=0

  while i < len(liste_evolue):
    if liste_evolue[i].isupper():
      maj+= 1
    i+= 2

  if maj > 5 and len(liste_evolue) > 10 :
    return("HELLO, WORLD !")

  return("Hello, world !")

# // TEST DES FEATURES //

def test_all_features():
  test_f1()
  print("la fonctionnalité 1 fonctionne comme prévu !")

  test_f2()
  print("la fonctionnalité 2 fonctionne comme prévu !")

  test_f3()
  print("la fonctionnalité 3 fonctionne comme prévu !")

  test_f4x5()
  print("les fonctionnalité 4 et 5 fonctionne comme prévu !")

  test_f6()
  print("la fonctionnalité 6 fonctionnent comme prévu !")

  test_f7()
  print("la fonctionnalité 7 fonctionnent comme prévu !")

  test_f8()
  print("la fonctionnalité 8 fonctionnent comme prévu !")

  test_f9()
  print("la fonctionnalité 9 fonctionnent comme prévu !")

  test_f10()
  print("la fonctionnalité 10 fonctionnent comme prévu !")

  test_sous_1_f11()
  print("la sous fonctionnalité sous_1_Feature11 fonctionnent comme prévu !")

  test_sous_2_f11()
  print("la sous fonctionnalité sous_2_Feature11 fonctionnent comme prévu !")

  test_f11()
  print("la fonctionnalité 11 fonctionnent comme prévu !")

  test_f12()
  print("la fonctionnalité 12 fonctionnent comme prévu !")

test_all_features()
