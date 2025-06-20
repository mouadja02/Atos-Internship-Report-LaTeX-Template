<p align="center">
  <a href="https://atos.net/en/">
    <img src="figs/Atos-logo.png" alt="Atos Logo" width="180"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="figs/logo_em.png" alt="School Logo" width="200"/>
</p>

# Guide d'utilisation du modèle de rapport de stage Atos

Ce document explique comment utiliser ce modèle LaTeX pour rédiger votre rapport de stage.

## Fonctionnalités du modèle

Ce modèle LaTeX offre de nombreuses fonctionnalités avancées :

- **Mise en page professionnelle** avec en-têtes et pieds de page personnalisés
- **Coloration syntaxique avancée** pour l'insertion de code (Java, Python, etc.)
- **Support des diagrammes TikZ** pour créer des schémas techniques
- **Gestion automatique** de la bibliographie et du glossaire
- **Styles de section personnalisés** avec couleurs (Rouge, Vert, Bleu)
- **Support multilingue** (français par défaut)
- **Intégration des logos** Atos et de votre école

## Structure du projet

Le projet est organisé comme suit :

- `main.tex`: Le fichier principal qui assemble toutes les parties du rapport. Vous y trouverez la configuration globale du document (packages, styles, coloration syntaxique, etc.).
- `title.tex`: La page de garde du rapport avec positionnement avancé des logos. Modifiez ce fichier pour changer le titre, votre nom, etc.
- `abstract.tex`: Fichier pour le résumé du rapport (optionnel).
- `glossary.tex`: Fichier pour définir les termes du glossaire.
- `ref.bib`: Fichier BibTeX pour les références bibliographiques.
- `figs/`: Dossier contenant toutes les images du rapport (logos Atos, images techniques, etc.).
- `codes/`: Dossier contenant des exemples de code (Java, Python) qui peuvent être référencés dans le rapport.
- `01_presentation_projet.tex`, `02_analyse_existant.tex`, ...: Fichiers de chapitre. Chaque fichier correspond à une section principale de votre rapport. C'est ici que vous rédigerez la majorité de votre contenu.
- `annexes.tex`: Pour le contenu des annexes.

## Comment modifier le contenu

### 1. Page de garde (`title.tex`)

Ouvrez `title.tex` et modifiez les champs suivants :
- Le titre du rapport (ligne avec "Sujet du stage")
- Votre nom et filière
- Le nom de vos tuteurs (entreprise et école)
- Les dates de stage (utilisez la commande `\periodeStage{date_début}{date_fin}`)

### 2. Résumé (`abstract.tex`)

Si vous souhaitez inclure un résumé, modifiez le fichier `abstract.tex` en remplaçant le commentaire par votre texte.

### 3. Contenu des chapitres

Pour chaque chapitre de votre rapport (Présentation du projet, Analyse de l'existant, etc.), ouvrez le fichier `.tex` correspondant (par exemple, `01_presentation_projet.tex`).

Remplacez les commentaires comme `% [Votre texte ici]` par votre propre texte.

### 4. Ajouter des images

1. Placez vos fichiers image dans le dossier `figs/`.
2. Dans votre fichier `.tex`, utilisez le code suivant pour insérer une image :

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\linewidth]{figs/votre_image.png}
    \caption{Légende de votre image.}
    \label{fig:votre_label}
\end{figure}
```
- Remplacez `votre_image.png` par le nom de votre fichier.
- Changez la `\caption` (légende) et le `\label` (pour les références croisées).

### 5. Créer des diagrammes TikZ

Le modèle inclut un support complet pour TikZ. Vous pouvez créer des diagrammes techniques directement dans LaTeX :

```latex
\begin{figure}[H]
    \centering
    \begin{tikzpicture}[node distance=2.5cm, auto]
        \tikzstyle{block} = [rectangle, draw, fill=blue!20, 
            text width=20em, text centered, rounded corners, minimum height=3em]
        \tikzstyle{line} = [draw, -{Latex}]
        
        \node [block] (data) {Source de Données};
        \node [block, below of=data] (process) {Traitement};
        
        \path [line] (data) -- (process);
    \end{tikzpicture}
    \caption{Exemple de diagramme TikZ.}
    \label{fig:mon_diagramme}
\end{figure}
```

### 6. Insérer du code avec coloration syntaxique

Le modèle inclut une configuration avancée pour l'affichage de code avec coloration syntaxique :

```latex
\begin{lstlisting}[language=Python, caption=Exemple de code Python]
import pandas as pd

def process_data(filename):
    df = pd.read_csv(filename)
    return df.dropna()
\end{lstlisting}
```

Vous pouvez également référencer des fichiers de code du dossier `codes/` :

```latex
\lstinputlisting[language=Java, caption=Code Java principal]{codes/main.java}
```

### 7. Bibliographie (`ref.bib`)

Pour ajouter une référence, ajoutez une entrée BibTeX dans `ref.bib`. Par exemple :

```bibtex
@book{goodfellow2016deep,
  title={Deep Learning},
  author={Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  publisher={MIT Press},
  year={2016}
}
```

Ensuite, dans votre texte, vous pouvez citer cette référence avec `\cite{goodfellow2016deep}`.

### 8. Glossaire (`glossary.tex`)

Pour ajouter un terme au glossaire, ajoutez une entrée dans `glossary.tex` :

```latex
\newglossaryentry{bigdata}{
    name={Big Data},
    description={Ensemble de données très volumineux qui dépasse les capacités des outils traditionnels de gestion de données.}
}
```

Utilisez `\gls{bigdata}` dans votre texte pour faire référence à ce terme.

## Utilisation avec Overleaf

La méthode recommandée pour éditer, prévisualiser et compiler ce rapport est d'utiliser [Overleaf](https://www.overleaf.com/).
Créez un compte, puis importez ce projet de l'une des manières suivantes :

### Option 1 : Méthode gratuite

1.  Sur la page de ce dépôt GitHub, cliquez sur le bouton vert `Code`, puis sur `Download ZIP`.
2.  Depuis votre tableau de bord Overleaf, cliquez sur **New Project**.
3.  Sélectionnez **Upload Project**.
4.  Chargez le fichier ZIP que vous venez de télécharger.

### Option 2 : Pour les utilisateurs Premium (via lien Git directement)

1.  Copiez l'URL de ce dépôt GitHub.
2.  Depuis votre tableau de bord Overleaf, cliquez sur **New Project**.
3.  Sélectionnez **Import from GitHub**.
4.  Collez l'URL du dépôt.

## Compilation en local

Pour générer le PDF, vous devez compiler le fichier `main.tex` avec un compilateur LaTeX (comme pdfLaTeX). Il est souvent nécessaire de compiler plusieurs fois pour que la table des matières, les références et le glossaire soient corrects.

**Séquence de compilation recommandée :**
1. `pdflatex main.tex`
2. `makeglossaries main`
3. `biber main` (ou `bibtex main`)
4. `pdflatex main.tex`
5. `pdflatex main.tex`

Si vous utilisez un éditeur LaTeX comme TeXstudio ou VS Code avec l'extension LaTeX Workshop, la compilation se fait généralement en un clic avec la séquence appropriée.

## Personnalisation avancée

### Couleurs des sections
Les couleurs des titres de section peuvent être modifiées dans `main.tex` :
- Sections principales : Rouge (Red)
- Sous-sections : Vert (Green)  
- Sous-sous-sections : Bleu (Blue)

### Style de code
Le style de coloration syntaxique peut être personnalisé en modifiant les définitions de couleurs dans `main.tex` :
- Arrière-plan : `codebg`
- Commentaires : `codegreen`
- Mots-clés : `codeblue`
- Chaînes : `codepurple`
