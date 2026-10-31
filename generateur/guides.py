# Articles du dossier /guides/. Le corps est en HTML simple (h2, p, ul, table).
# Textes vérifiés le 31/10/2026. Revoir la partie amende quand le décret d'application de la loi 2026-534 paraîtra.

GUIDES = [
dict(
  slug="duerp-obligatoire", court="Le DUERP est-il obligatoire ?",
  titre="DUERP obligatoire : qui est concerné et à partir de quand ?",
  desc="Le DUERP est obligatoire dès le premier salarié, apprenti compris, quel que soit le métier. Ce que dit la loi, ce que le document doit contenir et qui peut le consulter.",
  h1="Le DUERP est-il obligatoire ? Oui, dès le premier salarié",
  intro="Le document unique d'évaluation des risques professionnels (DUERP) est obligatoire pour toute entreprise qui emploie au moins une personne, apprenti compris. Le métier, le chiffre d'affaires ou le statut de l'entreprise n'y changent rien.",
  corps="""
<h2>Ce que dit la loi</h2>
<p>L'employeur doit évaluer les risques pour la santé et la sécurité de ses salariés (Code du travail, art. L4121-3). Les résultats de cette évaluation sont écrits dans un document unique (art. L4121-3-1 et R4121-1). Il n'y a pas de seuil : un seul salarié suffit, qu'il soit en CDI, en CDD, à temps partiel ou en apprentissage.</p>
<p>Un chef d'entreprise seul, sans salarié, n'est pas obligé de rédiger un DUERP. L'obligation commence à la première embauche.</p>

<h2>Ce que le document doit contenir</h2>
<ul>
<li><strong>Un inventaire des risques</strong> pour chaque unité de travail : un poste, un atelier, un chantier type, un véhicule. Les ambiances thermiques, comme la chaleur, en font partie.</li>
<li><strong>Une évaluation</strong> de chaque risque, en général selon sa gravité et sa fréquence, pour savoir par quoi commencer.</li>
<li><strong>Les actions de prévention</strong> à mener. Dans une entreprise de moins de 50 salariés, elles sont simplement listées dans le DUERP (art. L4121-3-1).</li>
<li><strong>Les données sur la pénibilité</strong> : les informations utiles pour savoir quels salariés sont exposés à des facteurs comme le bruit, les postures ou le travail de nuit (art. R4121-1-1).</li>
</ul>

<h2>Qui peut le consulter</h2>
<p>Le DUERP doit pouvoir être consulté par vos salariés, vos anciens salariés pour les versions qui les concernent, le médecin du travail, l'inspection du travail et la Carsat. Un affichage indique à vos salariés comment y accéder (art. R4121-4). Il est aussi transmis à votre service de santé au travail à chaque mise à jour.</p>

<h2>Combien de temps le garder</h2>
<p>Chaque version doit être conservée au moins 40 ans (art. L4121-3-1). Un dépôt sur un portail numérique est prévu par la loi, mais ce portail n'est pas encore ouvert : en attendant, vous gardez les versions dans l'entreprise, sur papier ou en fichier.</p>

<h2>Faire le sien soi-même ou se faire accompagner</h2>
<p>La loi n'impose pas de prestataire. Vous pouvez rédiger votre DUERP vous-même, avec un générateur en ligne ou un modèle. Ce qui compte, c'est que l'évaluation corresponde vraiment à votre entreprise. C'est là qu'un regard extérieur aide : poser les questions qu'on ne se pose plus, repérer les situations à risque devenues habituelles, et proposer des actions réalistes.</p>
""",
  faq=[
    ("Un apprenti compte-t-il comme salarié pour le DUERP ?", "Oui. Dès qu'un apprenti est embauché, le DUERP est obligatoire. Il doit même être plus précis si l'apprenti est mineur et affecté à des travaux réglementés."),
    ("Un stagiaire rend-il le DUERP obligatoire ?", "Le stagiaire n'est pas salarié, mais l'employeur reste responsable de sa sécurité dans ses locaux. Avoir un DUERP est fortement conseillé dans ce cas."),
    ("Le DUERP doit-il être signé ?", "La loi n'impose pas de signature, mais dater et signer chaque version permet de prouver quand l'évaluation a été faite."),
  ],
),
dict(
  slug="amende-duerp", court="Amende sans DUERP",
  titre="Amende DUERP 2026 : jusqu'à 4 000 € par salarié sans document unique",
  desc="Depuis le 27 juin 2026, l'absence de DUERP peut être sanctionnée par une amende administrative jusqu'à 4 000 € par salarié. Les sanctions, les cas concernés et comment les éviter.",
  h1="Amende sans DUERP : ce que vous risquez en 2026",
  intro="Depuis le 27 juin 2026, l'administration peut sanctionner directement une entreprise qui n'a pas de document unique, sans passer par un tribunal. L'amende peut atteindre 4 000 € par salarié. Voici ce qui a changé, et ce qui existait déjà.",
  corps="""
<h2>La nouvelle amende administrative</h2>
<p>La loi n° 2026-534 du 25 juin 2026 relative à la lutte contre les fraudes sociales et fiscales a ajouté l'absence de document unique à la liste des manquements que l'administration peut sanctionner elle-même (Code du travail, art. L8115-1).</p>
<ul>
<li><strong>Montant :</strong> jusqu'à 4 000 € par salarié concerné (art. L8115-3).</li>
<li><strong>Récidive :</strong> le plafond est doublé si le manquement se reproduit dans les deux ans.</li>
<li><strong>Qui la prononce :</strong> le directeur régional de l'économie, de l'emploi, du travail et des solidarités (DREETS), sur rapport de l'inspection du travail, après une procédure où vous pouvez présenter vos observations.</li>
<li><strong>Ce qui est visé :</strong> l'absence de DUERP. Un document qui existe mais n'est pas à jour relève de l'amende pénale ci-dessous.</li>
</ul>
<p>Pour une entreprise de 6 salariés, le plafond théorique atteint donc 24 000 €. Le montant réel dépend de la situation, de la bonne foi de l'employeur et de ses ressources.</p>

<h2>L'amende pénale, toujours en vigueur</h2>
<p>Ne pas rédiger ou ne pas mettre à jour son DUERP est aussi une contravention de 5<sup>e</sup> classe : jusqu'à 1 500 €, 3 000 € en récidive (art. R4741-1). Pour une société, le montant est multiplié par cinq, soit 7 500 €. Les deux amendes ne se cumulent pas pour les mêmes faits.</p>

<h2>En cas d'accident du travail</h2>
<p>C'est souvent le risque le plus lourd. Si un salarié est blessé et que le risque n'avait pas été évalué, la faute inexcusable de l'employeur est plus facile à retenir. Le salarié touche alors une rente majorée et une indemnisation complémentaire, que la Sécurité sociale récupère ensuite auprès de l'employeur.</p>

<h2>Devant les prud'hommes</h2>
<p>L'absence de DUERP est un manquement à l'obligation de sécurité de l'employeur. Elle est régulièrement invoquée par des salariés pour obtenir des dommages et intérêts, ou pour appuyer une prise d'acte de la rupture du contrat.</p>

<h2>Comment être tranquille</h2>
<ul>
<li>Avoir un DUERP qui décrit réellement votre entreprise, pas un modèle rempli à la va-vite.</li>
<li>Le dater, le garder, et afficher comment vos salariés peuvent le consulter.</li>
<li>Le mettre à jour après chaque changement important et après un accident, et chaque année à partir de 11 salariés.</li>
<li>Mener les actions prévues, ou au moins pouvoir montrer où vous en êtes.</li>
</ul>
""",
  faq=[
    ("L'amende de 4 000 € tombe-t-elle dès le premier contrôle ?", "Pas forcément. Après le rapport de l'inspection du travail, l'administration peut choisir entre un simple avertissement et une amende, après vous avoir laissé présenter vos observations. Elle tient compte de la bonne foi et des efforts engagés."),
    ("Un DUERP pas à jour expose-t-il à l'amende de 4 000 € ?", "Le texte vise l'absence de document. Un DUERP non mis à jour reste puni de l'amende pénale, jusqu'à 1 500 € ou 7 500 € pour une société."),
    ("Ces règles sont-elles définitives ?", "La loi est en vigueur depuis le 27 juin 2026. Un décret d'application peut encore préciser la procédure. Cette page sera mise à jour à sa parution."),
  ],
),
dict(
  slug="mise-a-jour-duerp", court="Mettre à jour son DUERP",
  titre="Mise à jour du DUERP : quand et comment la faire ?",
  desc="Quand faut-il mettre à jour son DUERP ? Chaque année à partir de 11 salariés, et pour tous après un changement important ou un accident. Les cas concrets et la marche à suivre.",
  h1="Mettre à jour son DUERP : quand et comment",
  intro="Un DUERP n'est pas un document qu'on rédige une fois pour toutes. La loi impose de le mettre à jour dans plusieurs situations, et un document dépassé ne protège ni vos salariés, ni vous en cas de contrôle.",
  corps="""
<h2>Les cas où la mise à jour est obligatoire</h2>
<p>Le Code du travail (art. R4121-2) prévoit trois situations :</p>
<ul>
<li><strong>Chaque année</strong>, si l'entreprise compte 11 salariés ou plus.</li>
<li><strong>Lors d'une décision d'aménagement important</strong> qui modifie les conditions de santé, de sécurité ou de travail.</li>
<li><strong>Quand une information nouvelle</strong> sur un risque est connue : un accident, une maladie professionnelle, un nouveau produit classé dangereux, une nouvelle réglementation.</li>
</ul>
<p>Dans une entreprise de moins de 11 salariés, il n'y a donc pas d'obligation annuelle, mais les deux autres cas s'appliquent.</p>

<h2>Des exemples concrets</h2>
<ul>
<li>Vous achetez une nouvelle machine, un engin ou un véhicule.</li>
<li>Vous embauchez sur un nouveau poste, ou un apprenti mineur.</li>
<li>Vous déménagez, agrandissez ou faites des travaux dans vos locaux.</li>
<li>Vous commencez une nouvelle activité : climatisation, rénovation de bâtiments anciens, moto à l'auto-école…</li>
<li>Un salarié a eu un accident, même sans arrêt de travail.</li>
<li>Une nouvelle règle s'applique, comme l'obligation d'évaluer le risque lié à la chaleur depuis le 1<sup>er</sup> juillet 2025.</li>
</ul>

<h2>Comment faire la mise à jour</h2>
<ul>
<li>Reprendre les unités de travail concernées par le changement.</li>
<li>Ajouter ou réévaluer les risques, et noter les mesures déjà prises.</li>
<li>Mettre à jour la liste des actions : ce qui est fait, ce qui reste à faire, qui s'en charge.</li>
<li>Créer une nouvelle version datée, et garder l'ancienne : chaque version se conserve 40 ans.</li>
<li>Transmettre la nouvelle version à votre service de santé au travail.</li>
</ul>

<h2>Combien ça coûte</h2>
<p>Si votre DUERP a été rédigé avec une structure claire, la mise à jour est rapide. Chez DUERP Conseil, une mise à jour après un changement coûte 99 €. Si vous avez un DUERP fait ailleurs, je peux aussi le relire et le compléter pour 99 €.</p>
""",
  faq=[
    ("Faut-il refaire tout le document à chaque mise à jour ?", "Non. On reprend seulement les parties concernées par le changement, puis on enregistre une nouvelle version datée."),
    ("Mon DUERP a cinq ans et rien n'a changé, est-il encore valable ?", "C'est rare que rien n'ait changé en cinq ans : réglementation, équipements, personnel. Une relecture permet de le vérifier et de prouver que l'évaluation a été revue."),
    ("Qui doit faire la mise à jour ?", "L'employeur en est responsable. Il peut se faire aider par un prestataire, son service de santé au travail ou un salarié désigné."),
  ],
),
dict(
  slug="duerp-ppsps", court="DUERP ou PPSPS ?",
  titre="DUERP et PPSPS : quelle différence pour une entreprise du bâtiment ?",
  desc="DUERP ou PPSPS ? Le DUERP concerne toute l'entreprise, le PPSPS un chantier précis. Qui doit faire quoi, quand, et comment l'un aide à rédiger l'autre.",
  h1="DUERP et PPSPS : deux documents, deux rôles",
  intro="Dans le bâtiment, on confond souvent les deux. Le DUERP est le document de votre entreprise, obligatoire dès le premier salarié. Le PPSPS est le document d'un chantier, demandé seulement sur certaines opérations. L'un ne remplace pas l'autre.",
  corps="""
<h2>Le DUERP : le document de votre entreprise</h2>
<p>Il décrit les risques de votre activité dans son ensemble : vos types de chantiers, votre dépôt ou atelier, vos véhicules, vos engins. Il est obligatoire dès le premier salarié (Code du travail, art. L4121-3 et R4121-1) et se met à jour quand votre activité change.</p>

<h2>Le PPSPS : le document d'un chantier</h2>
<p>Le plan particulier de sécurité et de protection de la santé est rédigé pour un chantier précis. Il est exigé de chaque entreprise qui intervient sur un chantier où un plan général de coordination (PGC SPS) est obligatoire : les opérations importantes soumises à déclaration préalable, ou celles qui comportent des travaux à risques particuliers (art. L4532-9 et R4532-56 et suivants). Il doit être remis au coordonnateur SPS avant le début des travaux.</p>

<h2>Le tableau pour s'y retrouver</h2>
<div class="cmp-wrap"><table class="cmp">
<thead><tr><th scope="col"></th><th scope="col">DUERP</th><th scope="col">PPSPS</th></tr></thead>
<tbody>
<tr><th scope="row">Pour quoi ?</th><td>Toute l'entreprise</td><td>Un chantier précis</td></tr>
<tr><th scope="row">Quand ?</th><td>Dès le premier salarié</td><td>Sur les chantiers avec coordination SPS et PGC</td></tr>
<tr><th scope="row">Pour qui ?</th><td>Vos salariés, l'inspection, la médecine du travail</td><td>Le coordonnateur SPS, le maître d'ouvrage</td></tr>
<tr><th scope="row">Durée de vie</th><td>Mis à jour en continu, versions gardées 40 ans</td><td>Le temps du chantier</td></tr>
</tbody>
</table></div>

<h2>Un bon DUERP fait gagner du temps sur les PPSPS</h2>
<p>Les risques de vos métiers, vos modes opératoires, vos équipements et vos formations sont déjà décrits dans le DUERP. Il ne reste plus qu'à les adapter au chantier : accès, coactivité, calendrier. Beaucoup d'artisans écrivent leurs PPSPS dans l'urgence, la veille d'un démarrage. Avec un DUERP solide, c'est l'affaire de quelques adaptations.</p>
""",
  faq=[
    ("Un PPSPS peut-il remplacer mon DUERP ?", "Non. Le PPSPS ne concerne qu'un chantier et disparaît avec lui. Le DUERP reste obligatoire pour l'entreprise, même si vous rédigez des PPSPS."),
    ("Je ne travaille que chez des particuliers, ai-je besoin d'un PPSPS ?", "Rarement : la plupart des petits chantiers chez les particuliers ne sont pas soumis au PPSPS. Le DUERP, lui, reste obligatoire dès le premier salarié."),
  ],
),
]
