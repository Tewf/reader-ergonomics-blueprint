# Blueprint

[![Vérifications contre reader-ergonomics](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-blueprint/)

Le raisonnement d'une personne écrit comme un arbre de topics, chaque partie avec un vérificateur, Lean d'abord pour la
logique. Un modèle de langue interprète les verdicts et oriente, pour que la personne ne se perde pas et que le
raisonnement se transmette. Les mathématiques formelles appellent un tel graphe d'affirmations vérifiées un
**blueprint**.

Cette page en anglais : [README.md](README.md). Les deux versions suivent le même état.

> **Audit (2026-11-03) :** la prose des trois affirmations a été vérifiée contre Euclide IX.20 (Joyce 1996) et sa variante
> factorielle (Wikipedia 2026 Euclid) par un modèle sur ordre du mainteneur, non par une personne ; les énoncés Lean attendent un lecteur de Lean.
>
> **État (2026-11-03), version 0.1.0 :** la revue de l'autoformalisation est faite, grise et formelle, 273 sources, et nomme sa
> référence, B1. B1 est construit en miniature, sauf le contrôle : le théorème d'Euclide en un sujet théorème et trois
> sujets d'énoncé, chacun nommant une déclaration Lean ([conception](design/first-build.md)), avec un fichier de défi
> qui tient les quatre énoncés à part des preuves ([0006](decisions/0006-a-challenge-file-holds-the-audited-statements.md)).
> Cinq vérifications tournent en CI : celle des topics, celle de l'énoncé, un contrôle du lien, un comparateur, et Lean.
> La [fiche](standard.md) tient cinq principes et une [forme](shapes/claim.md), l'énoncé. Le mainteneur
> n'a pas encore comparé les énoncés à leur source. Le modèle n'est pas encore dans la boucle. Le travail a commencé
> dans reader-ergonomics-topic et a migré ici avec son historique ([0001](decisions/0001-a-repository-of-its-own.md)).
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Les corrections sont bienvenues sous forme d'issues.

## L'adopter

Le blueprint est fait pour être copié et gardé comme le vôtre. Copiez-le depuis une version étiquetée
([tags](https://github.com/Tewf/reader-ergonomics-blueprint/tags)), pour qu'un changement ultérieur ici ne change
jamais votre copie.

1. Copiez [shapes/claim.md](shapes/claim.md), la forme, et les vérifications de [checks/local/](checks/local/) :
   `claim_shape.py`, `lean_link.py`, `comparator.py` et `topic.py`, aux mêmes chemins de votre dépôt.
2. Écrivez chaque étape de votre raisonnement comme un topic d'énoncé, et nommez une déclaration Lean sur sa ligne
   **Lean:**. Gardez les énoncés à contrôler dans un fichier de défi, à part des preuves, comme le fait
   [Blueprint/Challenge.lean](Blueprint/Challenge.lean).
3. Ajoutez `checks/config.toml` avec `extends = "reader-ergonomics"` et les tables de ce dépôt pour `[topic]`,
   `[claim_shape]`, `[lean_link]` et `[comparator]` ; réglez leurs chemins sur les vôtres.
4. Épinglez la norme par commit et lancez les vérifications, une seule commande :

   ```sh
   git clone https://github.com/Tewf/reader-ergonomics ../reader-ergonomics
   git -C ../reader-ergonomics checkout 2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a   # version 1.21.0
   python3 ../reader-ergonomics/checks/run.py chemin/vers/votre/dépôt
   ```

   Lean se construit à part, en CI, avec `lake build` ; les vérifications lisent les noms des déclarations et
   n'exécutent jamais Lean.

Un désaccord a trois destinations :

- votre style de lecteur, comme dérogation motivée, s'il porte sur votre lecteur ;
- une extension, s'il porte sur un genre ;
- une issue sur [ce dépôt](https://github.com/Tewf/reader-ergonomics-blueprint/issues), quand ses preuves ou sa forme sont fausses.


La section de la norme, [Take your own version](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/README.md#take-your-own-version), donne le reste.

## Où il se place

- **Il s'appuie sur le [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md)** (reader-ergonomics-topic v0.6.0) : chaque nœud d'un blueprint est
  un topic, avec son titre, son résumé, ses parties comme contenu et ce qu'il utilise comme liens.
- **Il obéit à [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/standard.md)** (v1.21.0) et exécute ses vérifications en CI.
- **Il ne pointe que vers le bas.** Les deux sont épinglés par commit ; aucun ne pointe vers ce dépôt.

## La boucle

![La personne écrit des topics ; les vérifications en CI renvoient leurs constats au modèle ; le modèle traduit un topic formel en Lean, qui renvoie erreurs et buts restés ouverts ; le modèle renvoie à la personne une orientation](loop.svg)

<details>
<summary>Source Graphviz</summary>

```dot
// The loop of the AI-augmented topic: the figure of ai-augmented/README.md.
// Colours: one per kind of part, the same in every figure of this extension; each kind is also named in its box.
// person orange, program blue, model green, proof assistant blue (a program); a back edge returns to its sender.
digraph loop {
  graph [rankdir=TB, nodesep=0.5, ranksep=0.55, bgcolor="white", pad=0.2, fontname="Inter"];
  node  [shape=box, style="rounded,filled", fontname="Inter", fontsize=13, margin="0.2,0.1", penwidth=1.5, fontcolor="#1F2328"];
  edge  [fontname="Inter", fontsize=11, color="#3D434B", fontcolor="#55575F", penwidth=1.3, arrowsize=0.8];
  P [label=<<b>person</b><br/><font point-size="11" color="#55575F">writes the idea as topics: one claim</font><br/><font point-size="11" color="#55575F">each, its summary, its parts</font>>, fillcolor="#FBEDE4", color="#B4541A", penwidth=2.6];
  C [label=<<b>checks, in CI</b><br/><font point-size="11" color="#55575F">the form: title, summary, one claim</font><br/><font point-size="11" color="#55575F">per topic, every part listed</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  M [label=<<b>model</b><br/><font point-size="11" color="#55575F">explains findings, proposes clearer</font><br/><font point-size="11" color="#55575F">wording; translates a formal topic</font><br/><font point-size="11" color="#55575F">into Lean</font>>, fillcolor="#E6F2EA", color="#2E7D4F"];
  L [label=<<b>proof assistant</b><br/><font point-size="11" color="#55575F">Lean checks the reasoning</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  P -> C [label=" topics"];
  C -> M [label=" findings"];
  M -> L [label=" Lean"];
  L -> M [label=" errors, goals\l left open\l"];
  M -> P [label=" guidance: what to split, what is\l unclear, what the proof assistant\l rejected, and why\l"];
}
```

</details>

La figure se lit de la personne vers le bas ; ce qui revient, erreurs et buts vers le modèle, orientation vers la
personne, remonte. Chaque partie a un rôle :

| Partie | Rôle | Décide |
|---|---|---|
| **personne** | possède le raisonnement ; écrit chaque étape comme un topic | ce qui est affirmé |
| **vérifications** | des programmes : la [vérification du topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/checks/local/topic.py) et celles de reader-ergonomics | si la forme est claire |
| **modèle** | un modèle de langue : explique, propose, traduit | rien : sa sortie est toujours vérifiée |
| **assistant de preuve** | Lean, pour ce qui est formalisé | si le raisonnement est valide |

## Périmètre

| | Quoi | Pourquoi |
|---|---|---|
| dedans | tout raisonnement ou toute création, écrit comme un arbre ou un graphe de topics | un topic peut porter toute information |
| dedans | les propriétés du topic sur chaque nœud : titre et résumé, parties comme contenu, usages comme liens, pas de cycle, trois niveaux en vue | la personne ne se perd pas, et le raisonnement se transmet |
| dedans | un vérificateur pour chaque partie | chaque affirmation est vérifiée là où elle se trouve, pas le tout à la fin |
| dedans | Lean comme oracle pour la logique et les preuves, premier et pour l'instant seul vérificateur du sens | son verdict est exact |
| dedans | le modèle comme interprète des verdicts et comme guide ; il ne décide rien et ne découpe jamais à la place de la personne | conditions 2 et 4 de la [position](evidence/autoformalization/position.md) de la revue |
| plus tard | d'autres vérificateurs (sources, tests, spécifications), après une revue des assurance cases | une affirmation découpée en sous-affirmations, chacune appuyée par une preuve, est ce que l'ingénierie des systèmes appelle un assurance case |
| dehors | construire un prouveur ou entraîner un modèle | d'autres le font ; ce dépôt s'en sert |
| dehors | le gabarit du topic lui-même | reader-ergonomics-topic le porte ; ce dépôt en épingle une version |

## Ce que la revue a trouvé

La [revue](evidence/autoformalization/) lit 80 sources grises et 182 formelles, et 11 liées depuis des revues voisines.

- Aucun programme ne décide si un énoncé formel dit ce que dit sa source ; la recherche le mesure contre des personnes
  ou contre un énoncé de référence vérifié.
- Les juges-modèles surestiment les traductions : un traducteur obtient 97,5 % selon son juge et 62,7 % selon des
  personnes. Les énoncés écrits à la main des benchmarks sont eux-mêmes faux dans 16,4 % et 38,5 % de deux benchmarks.
- Pour un modèle, le message d'erreur du vérificateur est ce qui fait marcher la réparation ; pour des personnes, aucune
  étude des messages d'un assistant de preuve n'a été trouvée.
- Découper le raisonnement en petites affirmations aide toujours la vérification, et la pensée seulement là où la
  personne a fait le découpage ; aucun essai randomisé n'a été trouvé.

## La référence

**B1, le blueprint audité** ([baseline](evidence/autoformalization/baseline.md)) :

- un blueprint de petits lemmes, chaque énoncé copié de sa source ;
- un modèle peut écrire les preuves, et ne décide rien ;
- Lean vérifie chaque soumission en CI, et comparator vérifie que chaque preuve prouve l'énoncé posé ;
- une personne contrôle chaque énoncé contre sa source.

## Suite

1. **Le contrôle de B1 :** le mainteneur compare chacun des quatre énoncés du
   [fichier de défi](Blueprint/Challenge.lean) à sa source et écrit la date sur la ligne **Audited:** du topic. Le
   comparateur et le fichier de défi sont en place ; le contrôle est la seule part de B1 qui manque.
2. **Ensuite la boucle :** la place du modèle, comme interprète et guide, mesurée contre B1.
3. **Avant tout vérificateur autre que Lean :** une revue des assurance cases, le nom que le domaine donne au cas
   général.

## Contenu

| Partie | Résumé |
|---|---|
| [standard](standard.md) | la fiche : cinq principes, deux sur l'énoncé qu'une personne contrôle et deux sur l'affirmation qu'elle écrit, chacun avec son grade |
| [principles](principles/) | un fichier par principe, avec sa thèse, son grade, ses preuves et sa vérification |
| [shapes](shapes/) | l'affirmation : le squelette d'une affirmation d'une preuve, avec les trois affirmations du théorème d'Euclide pour exemples |
| [design](design/) | les conceptions proposées avant une construction : la première est le théorème d'Euclide en sujets vérifiés par Lean |
| [proofs](proofs/infinitely-many-primes/) | le théorème d'Euclide en un sujet théorème et trois sujets d'énoncé, chacun nommant sa déclaration Lean |
| [evidence](evidence/) | la revue derrière le dépôt : l'autoformalisation, grise et formelle, et sa bibliographie |
| [decisions](decisions/) | un compte rendu par choix qui façonne ce dépôt, chacun ouvert par la décision en une phrase |

## Le vérifier

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py chemin/vers/ce/dépôt
```

La CI exécute les mêmes vérifications à chaque push, aux commits qu'épingle [checks.yml](.github/workflows/checks.yml).

## Licence

Code sous [Apache License 2.0](LICENSE) ; prose sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Réutilisez-le librement, en
citant ce dépôt ; [CITATION.cff](CITATION.cff) donne une citation si besoin.
