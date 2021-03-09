tekListe = [1,3,5,7,9,11,13,15,17,19]
ciftListe = [2,4,6,8,10,12,14,16,18,20]
liste = tekListe + ciftListe
bolunmusListe = []
for number in liste:
    bolunmusListe.append(number / 2)
    tipListe = [type(number) for number in bolunmusListe]
    print(tipListe)

#İlk defa kod yazdım, çok hoşuma gitti. Teşekkürler öğrettiğiniz için :^)

print("""\
    _-`````-,           ,- '- .
  .'   .- - |          | - -.  `.
 /.'  /                     `.   \
:/   :      _...   ..._      ``   :
::   :     /._ .`:'_.._\.    ||   :
::    `._ ./  ,`  :    \ . _.''   .
`:.      /   |  -.  \-. \\_      /
  \:._ _/  .'   .@)  \@) ` `\ ,.'
     _/,--'       .- .\,-.`--`.
       ,'/''     (( \ `  )    
        /'/'  \    `-'  (      
         '/''  `._,-----'
          ''/'    .,---'
           ''/'      ;:
             ''/''  ''/
               ''/''/''
                 '/'/'
                  `;

                    """)