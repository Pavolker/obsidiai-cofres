---
source: DATAGPT
conversation_id: 66ddf3b9-41d8-8002-b73c-baa90082b6a5
title: "UNIVERSO LITERATURA"
theme: ARTE CULTURA
created: 2024-09-08T18:58:01.421245Z
message_count: 6
attachments_count: 0
---

# UNIVERSO LITERATURA

- Tema: `ARTE CULTURA`
- Conversation ID: `66ddf3b9-41d8-8002-b73c-baa90082b6a5`

## Transcrição

### user

Faça uma lista dos 20 maiores autores de literatura, data de nascimento e morte e a sua principal obra, com data. Atenção: apenas literatura, ficção.

### assistant

Aqui está uma lista com 20 grandes autores de literatura de ficção, suas datas de nascimento e morte, e suas principais obras com as respectivas datas de publicação:

1. **William Shakespeare**  
   - Nascimento: 1564  
   - Morte: 1616  
   - Obra principal: *Hamlet* (1603)

2. **Miguel de Cervantes**  
   - Nascimento: 1547  
   - Morte: 1616  
   - Obra principal: *Dom Quixote* (1605)

3. **Léon Tolstói**  
   - Nascimento: 1828  
   - Morte: 1910  
   - Obra principal: *Guerra e Paz* (1869)

4. **Fiódor Dostoiévski**  
   - Nascimento: 1821  
   - Morte: 1881  
   - Obra principal: *Crime e Castigo* (1866)

5. **James Joyce**  
   - Nascimento: 1882  
   - Morte: 1941  
   - Obra principal: *Ulisses* (1922)

6. **Marcel Proust**  
   - Nascimento: 1871  
   - Morte: 1922  
   - Obra principal: *Em Busca do Tempo Perdido* (1913–1927)

7. **Herman Melville**  
   - Nascimento: 1819  
   - Morte: 1891  
   - Obra principal: *Moby Dick* (1851)

8. **Jane Austen**  
   - Nascimento: 1775  
   - Morte: 1817  
   - Obra principal: *Orgulho e Preconceito* (1813)

9. **Virginia Woolf**  
   - Nascimento: 1882  
   - Morte: 1941  
   - Obra principal: *Mrs. Dalloway* (1925)

10. **Franz Kafka**  
    - Nascimento: 1883  
    - Morte: 1924  
    - Obra principal: *A Metamorfose* (1915)

11. **Gabriel García Márquez**  
    - Nascimento: 1927  
    - Morte: 2014  
    - Obra principal: *Cem Anos de Solidão* (1967)

12. **Jorge Luis Borges**  
    - Nascimento: 1899  
    - Morte: 1986  
    - Obra principal: *Ficções* (1944)

13. **Charles Dickens**  
    - Nascimento: 1812  
    - Morte: 1870  
    - Obra principal: *David Copperfield* (1850)

14. **Mark Twain**  
    - Nascimento: 1835  
    - Morte: 1910  
    - Obra principal: *As Aventuras de Huckleberry Finn* (1884)

15. **Thomas Mann**  
    - Nascimento: 1875  
    - Morte: 1955  
    - Obra principal: *A Montanha Mágica* (1924)

16. **Haruki Murakami**  
    - Nascimento: 1949 (vivo)  
    - Obra principal: *Kafka à Beira-Mar* (2002)

17. **George Orwell**  
    - Nascimento: 1903  
    - Morte: 1950  
    - Obra principal: *1984* (1949)

18. **Toni Morrison**  
    - Nascimento: 1931  
    - Morte: 2019  
    - Obra principal: *Amada* (1987)

19. **Fyodor Dostoevsky**  
    - Nascimento: 1821  
    - Morte: 1881  
    - Obra principal: *Os Irmãos Karamázov* (1880)

20. **J.R.R. Tolkien**  
    - Nascimento: 1892  
    - Morte: 1973  
    - Obra principal: *O Senhor dos Anéis* (1954)

Esta lista é composta por autores de literatura de ficção cujas obras são amplamente reconhecidas como clássicos da literatura mundial.

### user

Faça, em VBA para o power point, um slide com essas 20 referências, colocando cada uma delas em uma caixa de texto

### assistant

Aqui está um código VBA para o PowerPoint que cria um slide com as 20 referências em caixas de texto. O código insere uma nova apresentação e preenche o slide com os autores e suas informações.

### Código VBA:

```vba
Sub CriarSlideComAutores()
    ' Cria uma nova apresentação
    Dim ppt As PowerPoint.Application
    Dim pres As PowerPoint.Presentation
    Dim slide As PowerPoint.Slide
    Dim caixaTexto As PowerPoint.Shape
    Dim i As Integer
    Dim topPosition As Single
    Dim leftPosition As Single
    Dim height As Single
    Dim width As Single
    
    ' Abre o PowerPoint
    Set ppt = New PowerPoint.Application
    Set pres = ppt.Presentations.Add
    ppt.Visible = True
    
    ' Adiciona um slide
    Set slide = pres.Slides.Add(1, ppLayoutText)
    
    ' Define o texto com autores e obras
    Dim referencias(1 To 20) As String
    referencias(1) = "1. William Shakespeare (1564–1616) - *Hamlet* (1603)"
    referencias(2) = "2. Miguel de Cervantes (1547–1616) - *Dom Quixote* (1605)"
    referencias(3) = "3. Léon Tolstói (1828–1910) - *Guerra e Paz* (1869)"
    referencias(4) = "4. Fiódor Dostoiévski (1821–1881) - *Crime e Castigo* (1866)"
    referencias(5) = "5. James Joyce (1882–1941) - *Ulisses* (1922)"
    referencias(6) = "6. Marcel Proust (1871–1922) - *Em Busca do Tempo Perdido* (1913-1927)"
    referencias(7) = "7. Herman Melville (1819–1891) - *Moby Dick* (1851)"
    referencias(8) = "8. Jane Austen (1775–1817) - *Orgulho e Preconceito* (1813)"
    referencias(9) = "9. Virginia Woolf (1882–1941) - *Mrs. Dalloway* (1925)"
    referencias(10) = "10. Franz Kafka (1883–1924) - *A Metamorfose* (1915)"
    referencias(11) = "11. Gabriel García Márquez (1927–2014) - *Cem Anos de Solidão* (1967)"
    referencias(12) = "12. Jorge Luis Borges (1899–1986) - *Ficções* (1944)"
    referencias(13) = "13. Charles Dickens (1812–1870) - *David Copperfield* (1850)"
    referencias(14) = "14. Mark Twain (1835–1910) - *As Aventuras de Huckleberry Finn* (1884)"
    referencias(15) = "15. Thomas Mann (1875–1955) - *A Montanha Mágica* (1924)"
    referencias(16) = "16. Haruki Murakami (1949–) - *Kafka à Beira-Mar* (2002)"
    referencias(17) = "17. George Orwell (1903–1950) - *1984* (1949)"
    referencias(18) = "18. Toni Morrison (1931–2019) - *Amada* (1987)"
    referencias(19) = "19. Fyodor Dostoevsky (1821–1881) - *Os Irmãos Karamázov* (1880)"
    referencias(20) = "20. J.R.R. Tolkien (1892–1973) - *O Senhor dos Anéis* (1954)"
    
    ' Configurações de posição e dimensões das caixas de texto
    topPosition = 50
    leftPosition = 50
    height = 20
    width = 600
    
    ' Adiciona cada referência em uma nova caixa de texto no slide
    For i = 1 To 20
        Set caixaTexto = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, leftPosition, topPosition, width, height)
        caixaTexto.TextFrame.TextRange.Text = referencias(i)
        caixaTexto.TextFrame.TextRange.Font.Size = 12
        caixaTexto.TextFrame.TextRange.Font.Name = "Arial"
        topPosition = topPosition + 25 ' Ajusta a posição vertical para cada nova caixa
    Next i
    
End Sub
```

### Instruções:
1. Abra o PowerPoint.
2. Pressione `Alt + F11` para abrir o Editor do VBA.
3. No menu, vá em `Inserir` -> `Módulo`.
4. Cole o código acima no módulo.
5. Pressione `F5` para executar o código.

Esse código cria uma nova apresentação do PowerPoint e insere um slide com caixas de texto, cada uma contendo uma das 20 referências. O layout do slide é ajustado para comportar todas as entradas com espaçamento adequado.

### user

refaça esse código, colocando cada caixa de texto com o tamanho 7cm x 2cm, sendo 4 caixas de texto por linha, em 5 colunas

### assistant

Aqui está a versão atualizada do código VBA para o PowerPoint que cria caixas de texto de 7 cm de largura por 2 cm de altura, organizadas em 4 caixas por linha e 5 linhas:

### Código VBA:

```vba
Sub CriarSlideComAutoresOrganizados()
    ' Cria uma nova apresentação
    Dim ppt As PowerPoint.Application
    Dim pres As PowerPoint.Presentation
    Dim slide As PowerPoint.Slide
    Dim caixaTexto As PowerPoint.Shape
    Dim i As Integer
    Dim topPosition As Single
    Dim leftPosition As Single
    Dim height As Single
    Dim width As Single
    Dim linha As Integer
    Dim coluna As Integer
    
    ' Abre o PowerPoint
    Set ppt = New PowerPoint.Application
    Set pres = ppt.Presentations.Add
    ppt.Visible = True
    
    ' Adiciona um slide
    Set slide = pres.Slides.Add(1, ppLayoutBlank)
    
    ' Define o texto com autores e obras
    Dim referencias(1 To 20) As String
    referencias(1) = "1. William Shakespeare (1564–1616) - *Hamlet* (1603)"
    referencias(2) = "2. Miguel de Cervantes (1547–1616) - *Dom Quixote* (1605)"
    referencias(3) = "3. Léon Tolstói (1828–1910) - *Guerra e Paz* (1869)"
    referencias(4) = "4. Fiódor Dostoiévski (1821–1881) - *Crime e Castigo* (1866)"
    referencias(5) = "5. James Joyce (1882–1941) - *Ulisses* (1922)"
    referencias(6) = "6. Marcel Proust (1871–1922) - *Em Busca do Tempo Perdido* (1913-1927)"
    referencias(7) = "7. Herman Melville (1819–1891) - *Moby Dick* (1851)"
    referencias(8) = "8. Jane Austen (1775–1817) - *Orgulho e Preconceito* (1813)"
    referencias(9) = "9. Virginia Woolf (1882–1941) - *Mrs. Dalloway* (1925)"
    referencias(10) = "10. Franz Kafka (1883–1924) - *A Metamorfose* (1915)"
    referencias(11) = "11. Gabriel García Márquez (1927–2014) - *Cem Anos de Solidão* (1967)"
    referencias(12) = "12. Jorge Luis Borges (1899–1986) - *Ficções* (1944)"
    referencias(13) = "13. Charles Dickens (1812–1870) - *David Copperfield* (1850)"
    referencias(14) = "14. Mark Twain (1835–1910) - *As Aventuras de Huckleberry Finn* (1884)"
    referencias(15) = "15. Thomas Mann (1875–1955) - *A Montanha Mágica* (1924)"
    referencias(16) = "16. Haruki Murakami (1949–) - *Kafka à Beira-Mar* (2002)"
    referencias(17) = "17. George Orwell (1903–1950) - *1984* (1949)"
    referencias(18) = "18. Toni Morrison (1931–2019) - *Amada* (1987)"
    referencias(19) = "19. Fyodor Dostoevsky (1821–1881) - *Os Irmãos Karamázov* (1880)"
    referencias(20) = "20. J.R.R. Tolkien (1892–1973) - *O Senhor dos Anéis* (1954)"
    
    ' Define as dimensões das caixas de texto
    width = 7 * 28.3465 ' 7 cm convertidos em pontos
    height = 2 * 28.3465 ' 2 cm convertidos em pontos
    
    ' Posições iniciais
    topPosition = 50 ' Posição inicial vertical
    leftPosition = 50 ' Posição inicial horizontal
    
    ' Adiciona as caixas de texto organizadas em 4 colunas e 5 linhas
    For i = 1 To 20
        ' Calcula a linha e a coluna
        linha = ((i - 1) \\ 4) + 1
        coluna = ((i - 1) Mod 4) + 1
        
        ' Define a posição de cada caixa de texto com base na linha e coluna
        leftPosition = 50 + (coluna - 1) * (width + 20) ' Distância horizontal entre as caixas
        topPosition = 50 + (linha - 1) * (height + 20) ' Distância vertical entre as caixas
        
        ' Adiciona a caixa de texto
        Set caixaTexto = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, leftPosition, topPosition, width, height)
        caixaTexto.TextFrame.TextRange.Text = referencias(i)
        caixaTexto.TextFrame.TextRange.Font.Size = 12
        caixaTexto.TextFrame.TextRange.Font.Name = "Arial"
        caixaTexto.TextFrame.VerticalAnchor = msoAnchorMiddle ' Centraliza verticalmente o texto
        caixaTexto.TextFrame.TextRange.ParagraphFormat.Alignment = ppAlignCenter ' Centraliza o texto
    Next i
    
End Sub
```

### Instruções:

1. Abra o PowerPoint.
2. Pressione `Alt + F11` para abrir o Editor do VBA.
3. No menu, vá em `Inserir` -> `Módulo`.
4. Cole o código acima no módulo.
5. Pressione `F5` para executar o código.

### Explicação:

- Cada caixa de texto tem as dimensões de **7 cm x 2 cm**, convertidas em pontos (1 cm = 28,3465 pontos).
- O layout das caixas de texto é organizado em 4 colunas e 5 linhas, com uma margem de 20 pontos entre cada caixa de texto.
- As caixas de texto são centralizadas, tanto horizontalmente quanto verticalmente, dentro das suas dimensões.

Este código criará um slide com 20 caixas de texto contendo os autores e suas obras, organizadas em um layout de 4 caixas por linha e 5 linhas.
