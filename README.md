###### NUME: POPA VICTOR-ANDREI
###### GRUPA: 313CA

FRONTEND:
Interfața de utilizator este construită folosind HTML si CSS, cu
ajutorul framework-ului Bootstrap pentru a asigura un aspect modern
și responsiv. Acest README oferă o scurtă prezentare a fiecărei pagini
și a funcționalităților sale.
Pagina Principală (Galerie Foto)

    Descriere: Pagina principală afișează galeria publică de fotografii.
    Vizitatorii pot vizualiza miniaturile fotografiilor și pot face clic
    pe fiecare fotografie pentru a o vedea în dimensiunea sa completă.
    Funcționalități:
        Vizualizarea galeriei publice de fotografii.
        Vizualizarea miniaturilor fotografiilor.
        Deschiderea fotografiilor în dimensiunea completă la clic pe
        fiecare fotografie.

Pagina de Autentificare (Login)

    Descriere: Pagina de autentificare permite administratorului să se
    autentifice în sistem pentru a avea acces la funcționalitățile
    administrative, cum ar fi încărcarea de noi fotografii.
    Funcționalități:
        Formular de autentificare pentru administrator.
        Validare acreditivele de autentificare.
        Redirecționare către pagina de încărcare după autentificare reușită.

Pagina de Încărcare (Upload)

    Descriere: Pagina de încărcare permite administratorului să încarce noi
    fotografii în galerie.
    Funcționalități:
        Formular de încărcare a fotografiilor.
        Câmpuri opționale pentru redenumirea fotografiilor și specificarea
        categoriilor.
        Validare și gestionare a încărcării fotografiilor.

Tehnologii Folosite

    Python: Limbajul de programare folosit pentru dezvoltarea backend-ului.
    Flask: Framework-ul web pentru Python folosit pentru construirea și
    gestionarea serverului web.
    RESTful API: API-ul web conform principiilor REST pentru comunicarea
    cu partea de frontend și alte servicii.

Funcționalități Principale

    Autentificare: Gestionarea autentificării utilizatorilor, inclusiv
    verificarea credențialelor și gestionarea sesiunilor de autentificare.
    Încărcare Fotografii: Procesarea și stocarea fotografiilor încărcate
    de utilizatori în galerie.
    Ștergere Fotografii: Funcționalitate pentru ștergerea fotografiilor din galerie.

Configurare și Instalare

    Asigurați-vă că aveți Python și pip instalate pe sistemul dumneavoastră.
    Creați și activați un mediu virtual Python (opțional, dar recomandat).
    Instalați dependențele backend folosind pip install -r requirements.txt.
    Porniți serverul backend folosind python app.py.

Structura Dockerfile

    Base Image: Specifică imaginea de bază pe care o folosește Dockerfile-ul
    pentru construirea imaginii Docker. De obicei, se folosește o imagine
    existentă care conține mediul de execuție necesar pentru aplicație.
    WORKDIR: Setează directorul de lucru în interiorul containerului, unde
    vor fi copiate și executate toate comenzile următoare.
    COPY: Copiază fișierele necesare din directorul local în directorul de
    lucru al containerului.
    RUN: Rulează comenzi pentru instalarea dependențelor și configurarea
    aplicației în interiorul containerului.
    EXPOSE: Specifică portul pe care aplicația va asculta conexiuni.
    CMD: Specifică comanda implicită care va fi executată atunci când
    containerul este pornit.


