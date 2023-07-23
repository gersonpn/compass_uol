# <span style="color: red;"> **__Trilha de estudos do programa de estágio e bolsas AWS Cloud Data Engineering__**


# <span style="color: green;"> __Sprint 1__

# Git e GitHub: Conceitos e Comandos Básicos



# Trilha de estudos do programa de estágio e bolsas AWS Cloud Data Engineering

## Git e GitHub: Conceitos e Comandos Básicos

### 1. Inicializando um Repositório Local

Para começar a usar o Git em seu projeto, você deve inicializar um repositório local com o comando `git init`. Isso criará um repositório vazio na pasta atual do projeto.

### 2. Adicionando e Comitando Arquivos

Use `git add` para adicionar os arquivos que deseja incluir no controle de versão.

- `git add .` adiciona todos os arquivos modificados na pasta atual.
- `git add <nome do arquivo>` adiciona um arquivo específico ao repositório.

Para registrar as alterações no repositório, faça um commit com uma mensagem descritiva usando `git commit -m "Mensagem descrevendo as alterações"`.

### 3. Conectando ao Repositório Remoto

Antes de enviar os arquivos para o GitHub, conecte seu repositório local ao repositório remoto usando `git remote add origin <url do repositório>`. O repositório remoto é onde o código será armazenado na plataforma.

### 4. Enviando e Atualizando o Repositório Remoto

Para enviar os arquivos pela primeira vez, utilize `git push -u origin main`.

Após o primeiro push, os comandos para enviar alterações subsequentes são:

- `git add .`
- `git commit -m "Mensagem descrevendo as alterações"`
- `git push`

### 5. Clone e Pull

Para obter uma cópia de um repositório remoto para o seu computador, utilize `git clone <url do repositório>`.

Para obter as últimas alterações do repositório remoto e sincronizá-las com o seu repositório local, use `git pull`.

### 6. Removendo Arquivos

Para remover arquivos do controle de versão e do repositório, utilize `git rm <nome do arquivo>`.

### 7. Histórico e Informações

Visualize o histórico de commits do repositório usando `git log`.

### 8. Movendo e Renomeando Arquivos

Utilize `git mv <nome do arquivo antigo> <nome do arquivo novo>` para mover ou renomear arquivos no repositório.

### 9. Desfazendo Alterações

Para desfazer alterações em arquivos antes do commit, use `git checkout -- <nome do arquivo>`.

### 10. Arquivos Ignorados com .gitignore

Crie um arquivo `.gitignore` para especificar quais arquivos e pastas devem ser ignorados pelo Git e não serão rastreados pelo controle de versão.

### 11. Git Reset

O comando `git reset` permite desfazer commits e alterações em seu repositório.

- `git reset HEAD~1` desfaz o commit, mantendo as alterações no working directory.
- `git reset --hard HEAD~1` desfaz o commit e descarta as alterações no working directory.

### 12. Branches

Branches são linhas de desenvolvimento independentes que permitem trabalhar em funcionalidades ou correções separadamente.

- `git branch <nome da branch>` cria uma nova branch.
- `git checkout <nome da branch>` muda para uma branch existente.
- `git checkout -b <nome da branch>` cria e muda para uma nova branch.
- `git branch -d <nome da branch>` exclui uma branch.

### 13. Git Stash

O comando `git stash` é útil quando você precisa salvar temporariamente as alterações atuais sem fazer um commit.

- `git stash` salva as alterações em um stash.
- `git stash list` lista os stashes salvos.
- `git stash apply stash@{n}` aplica um stash específico.
- `git stash drop stash@{n}` remove um stash específico.
- `git stash pop` aplica e remove o stash mais recente.

### 14. Git Submodule

Git submodule é usado para incluir um repositório Git dentro de outro repositório Git.

- `git submodule add <URL do repositório>` adiciona um submodule ao seu repositório.
- `git submodule init` inicializa os submódulos após o clone.
- `git submodule update` atualiza os submódulos existentes para as versões corretas.

### 15. Git Show

O comando `git show` é usado para exibir informações sobre um commit específico ou um objeto do Git.

- `git show` exibe detalhes sobre o último commit.
- `git show <hash do commit>` exibe informações detalhadas sobre o commit especificado.

### 16. Git Diff

O comando `git diff` mostra as diferenças entre commits, o working directory e o index.

- `git diff` mostra as diferenças entre o working directory e o index.
- `git diff <commit1>..<commit2>` mostra as diferenças entre dois commits.
- `git diff --staged` mostra as diferenças entre o index e o último commit.

### 17. Git Shortlog

O comando `git shortlog` gera um resumo de log legível por humanos de commits.

- `git shortlog` mostra um resumo de log para todos os commits do repositório.
- `git shortlog -s` mostra apenas o número de commits feitos por cada autor.
- `git shortlog -n` mostra o resumo em ordem numérica, em vez de alfabética.
