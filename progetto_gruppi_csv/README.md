# Calcolo sottogruppi

## Introduzione

Questo programma permette di partizionare un'insieme di ``n`` persone
in 2 gruppi di uguale dimensione massimizzando l'efficienza di entrambi i gruppi.

Ogni persona fornirebbe un certo aiuto (quantificato in punti) ad ogni altra persona se si trovasse nello stesso gruppo.

L'input del programma è una tabella di numeri interi codificata in CSV tale che il numero alla riga ``i``, colonna ``j`` indica quanti punti la persona ``i`` fornirebbe alla persona ``j`` se si trovassero nello stesso gruppo. La tabella deve avere quadrata.

## Obiettivo

Dato ``T1`` (risp. ``T2``) la sottotabella ottenuta filtrando solo le persone del primo (risp. secondo) gruppo, l'efficienza viene quantificata in un numero indicante la media tra la somma dei numeri della sottotabella ``T1`` e la somma dei numeri della sottotabella ``T2`` ponderata per il numero di partecipanti.

L'obiettivo è trovare il partizionamento che massimizza la media (ovvero l'efficienza).

## Funzionamento

Il programma legge il file CSV (passatogli come argomento) aspettandosi di trovare una tabella quadrata di numeri interi di dimensione massima 26x26.

Dopo aver convertito il file CSV in una matrice come lista di liste per riga di dimensione ``n``, il programma per ogni combinazione di numeri da 0 a ``n`` aggiorna le variabili che memorizzano:

- il miglior gruppo 1
- il miglior gruppo 2 (il complementare del primo)
- la somma della miglior combinazione dei 2 gruppi ottenuta come la somma tra le celle di ``T1`` diviso il numero di partecipanti del primo gruppo e le celle di ``T2`` diviso il numero di partecipanti del secondo gruppo

se la somma della combinazione di gruppi presa in considerazione è maggiore della somma della attuale miglior combinazione.

> Nota: la somma è diversa dalla media, però massimizzare la somma equivale a massimizzare la media. Per motivi di efficienza si utilizza la somma.

Per il prossimo passo viene assegnata una lettera ad ogni persona a partire dalla ``A`` in ordine alfabetico, e viene mostrato a video il partizionamento unendo le lettere delle persone dello stesso gruppo e separando i 2 gruppi da uno spazio.
Nella seconda riga viene stampato, invece, la media pei punti offerti.

## Esempio

|   | A | B | C | D |
|---|---|---|---|---|
| A |   | 2 | 13| 4 |
| B | 5 |   | 7 | 16|
| C | 18| 10|   | 12|
| D | 13| 14| 15|   |

```bash
AC BD
15.25
```
