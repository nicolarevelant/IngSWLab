# Calcolo sottogruppi

## Introduzione

Questo programma permette di partizionare un'insieme di ``n`` persone
in 2 gruppi di uguale dimensione massimizzando l'efficienza di entrambi i gruppi.

Ogni persona fornirebbe un certo aiuto (quantificato in punti) ad ogni altra persona se si trovasse nello stesso gruppo.

L'input del programma è una tabella di numeri interi codificata in CSV tale che il numero alla riga ``i``, colonna ``j`` indica quanti punti la persona ``i`` fornirebbe alla persona ``j`` se si trovassero nello stesso gruppo. La tabella deve avere dimensione pari.

## Obiettivo

Dato ``T1`` (risp. ``T2``) la sottotabella ottenuta filtrando solo le persone del primo (risp. secondo) gruppo, l'efficienza viene quantificata in un numero indicante la media tra la somma dei numeri della sottotabella ``T1`` e la somma dei numeri della sottotabella ``T2``.

L'obiettivo è trovare il partizionamento che massimizza l'efficienza.

## Funzionamento

Il programma legge il file CSV (passatogli come argomento) aspettandosi di trovare una tabella quadrata di numeri interi di dimensione massima 26x26.

Viene assegnata una lettera ad ogni persona a partire dalla ``A`` in ordine alfabetico.

TODO: completare

Viene restituito il partizionamento unendo le lettere delle persone dello stesso gruppo e separando i 2 gruppi da uno spazio.

Esempio (senza virgolette): "ABC DEF"

## Esempio

|   | A | B | C | D |
|---|---|---|---|---|
| A |   | 2 | 3 | 4 |
| B | 5 |   | 7 | 8 |
| C | 9 | 10|   | 12|
| D | 13| 14| 15|   |
