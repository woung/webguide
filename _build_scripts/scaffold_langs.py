import json, os, re

manifest = json.load(open('manifest.json'))

TITLES = {
  'fr': {
    'Acknowledgments': 'Remerciements',
    'Abbreviations': 'Abréviations',
    'Executive summary': 'Résumé analytique',
    'Introduction': 'Introduction',
    'Setting up your EWARS account': 'Configuration de votre compte EWARS',
    'Data Collection and Monitoring': 'Collecte et suivi des données',
    'Data analysis, visualization and dissemination': 'Analyse, visualisation et diffusion des données',
    'Chapter 1. Overview of EWARS in a box': "Chapitre 1. Aperçu d'EWARS in a box",
    'Chapter 2. Getting started': 'Chapitre 2. Prise en main',
    'Chapter 3. Locations': 'Chapitre 3. Emplacements',
    'Chapter 4. Configuration Transfer': 'Chapitre 4. Transfert de configuration',
    'Chapter 5. Indicators': 'Chapitre 5. Indicateurs',
    'Chapter 6. Forms': 'Chapitre 6. Formulaires',
    'Chapter 7. Alarms': 'Chapitre 7. Alarmes',
    'Chapter 8. Users and their assignments': 'Chapitre 8. Utilisateurs et leurs affectations',
    'Chapter 9. User profiles, tasks and notifications': 'Chapitre 9. Profils utilisateurs, tâches et notifications',
    'Chapter 10. EWARS account settings': 'Chapitre 10. Paramètres du compte EWARS',
    'Chapter 11. Report manager': 'Chapitre 11. Gestionnaire de rapports',
    'Chapter 12. M&E Auditor': 'Chapitre 12. Auditeur S&E',
    'Chapter 13. Alert log': 'Chapitre 13. Journal des alertes',
    'Chapter 14. Data Import': 'Chapitre 14. Importation de données',
    'Chapter 15. Plot': 'Chapitre 15. Graphique',
    'Chapter 16. Mapping': 'Chapitre 16. Cartographie',
    'Chapter 17. Widgets and their configuration': 'Chapitre 17. Widgets et leur configuration',
    'Chapter 18. Notebooks': 'Chapitre 18. Carnets',
    'Chapter 19. Dashboards': 'Chapitre 19. Tableaux de bord',
    'Chapter 20. Outbreaks': 'Chapitre 20. Flambées épidémiques',
    'Chapter 21. Documents and Document Templates': 'Chapitre 21. Documents et modèles de documents',
    'Chapter 22. Website Builder': 'Chapitre 22. Générateur de site web',
    'Chapter 23. Export': 'Chapitre 23. Exportation',
    'Chapter 24. SMS reporting and teams': 'Chapitre 24. Notification par SMS et équipes',
    'Chapter 25. EWARS Stand-alone': 'Chapitre 25. EWARS Autonome',
    'Chapter 26. Glossary': 'Chapitre 26. Glossaire',
    'Chapter 27. Help and support': 'Chapitre 27. Aide et assistance',
  },
  'es': {
    'Acknowledgments': 'Agradecimientos',
    'Abbreviations': 'Abreviaturas',
    'Executive summary': 'Resumen ejecutivo',
    'Introduction': 'Introducción',
    'Setting up your EWARS account': 'Configuración de su cuenta EWARS',
    'Data Collection and Monitoring': 'Recopilación y monitoreo de datos',
    'Data analysis, visualization and dissemination': 'Análisis, visualización y difusión de datos',
    'Chapter 1. Overview of EWARS in a box': 'Capítulo 1. Panorama general de EWARS in a box',
    'Chapter 2. Getting started': 'Capítulo 2. Primeros pasos',
    'Chapter 3. Locations': 'Capítulo 3. Ubicaciones',
    'Chapter 4. Configuration Transfer': 'Capítulo 4. Transferencia de configuración',
    'Chapter 5. Indicators': 'Capítulo 5. Indicadores',
    'Chapter 6. Forms': 'Capítulo 6. Formularios',
    'Chapter 7. Alarms': 'Capítulo 7. Alarmas',
    'Chapter 8. Users and their assignments': 'Capítulo 8. Usuarios y sus asignaciones',
    'Chapter 9. User profiles, tasks and notifications': 'Capítulo 9. Perfiles de usuario, tareas y notificaciones',
    'Chapter 10. EWARS account settings': 'Capítulo 10. Configuración de la cuenta EWARS',
    'Chapter 11. Report manager': 'Capítulo 11. Administrador de informes',
    'Chapter 12. M&E Auditor': 'Capítulo 12. Auditor de M&E',
    'Chapter 13. Alert log': 'Capítulo 13. Registro de alertas',
    'Chapter 14. Data Import': 'Capítulo 14. Importación de datos',
    'Chapter 15. Plot': 'Capítulo 15. Gráfico',
    'Chapter 16. Mapping': 'Capítulo 16. Mapeo',
    'Chapter 17. Widgets and their configuration': 'Capítulo 17. Widgets y su configuración',
    'Chapter 18. Notebooks': 'Capítulo 18. Cuadernos',
    'Chapter 19. Dashboards': 'Capítulo 19. Paneles de control',
    'Chapter 20. Outbreaks': 'Capítulo 20. Brotes',
    'Chapter 21. Documents and Document Templates': 'Capítulo 21. Documentos y plantillas de documentos',
    'Chapter 22. Website Builder': 'Capítulo 22. Creador de sitios web',
    'Chapter 23. Export': 'Capítulo 23. Exportación',
    'Chapter 24. SMS reporting and teams': 'Capítulo 24. Notificación por SMS y equipos',
    'Chapter 25. EWARS Stand-alone': 'Capítulo 25. EWARS Independiente',
    'Chapter 26. Glossary': 'Capítulo 26. Glosario',
    'Chapter 27. Help and support': 'Capítulo 27. Ayuda y soporte',
  },
  'ar': {
    'Acknowledgments': 'شكر وتقدير',
    'Abbreviations': 'المختصرات',
    'Executive summary': 'الملخص التنفيذي',
    'Introduction': 'مقدمة',
    'Setting up your EWARS account': 'إعداد حساب EWARS الخاص بك',
    'Data Collection and Monitoring': 'جمع البيانات ورصدها',
    'Data analysis, visualization and dissemination': 'تحليل البيانات وتصورها ونشرها',
    'Chapter 1. Overview of EWARS in a box': 'الفصل 1. نظرة عامة على EWARS in a box',
    'Chapter 2. Getting started': 'الفصل 2. البدء',
    'Chapter 3. Locations': 'الفصل 3. المواقع',
    'Chapter 4. Configuration Transfer': 'الفصل 4. نقل الإعدادات',
    'Chapter 5. Indicators': 'الفصل 5. المؤشرات',
    'Chapter 6. Forms': 'الفصل 6. النماذج',
    'Chapter 7. Alarms': 'الفصل 7. الإنذارات',
    'Chapter 8. Users and their assignments': 'الفصل 8. المستخدمون ومهامهم',
    'Chapter 9. User profiles, tasks and notifications': 'الفصل 9. ملفات تعريف المستخدمين والمهام والإشعارات',
    'Chapter 10. EWARS account settings': 'الفصل 10. إعدادات حساب EWARS',
    'Chapter 11. Report manager': 'الفصل 11. مدير التقارير',
    'Chapter 12. M&E Auditor': 'الفصل 12. مدقق الرصد والتقييم',
    'Chapter 13. Alert log': 'الفصل 13. سجل التنبيهات',
    'Chapter 14. Data Import': 'الفصل 14. استيراد البيانات',
    'Chapter 15. Plot': 'الفصل 15. الرسم البياني',
    'Chapter 16. Mapping': 'الفصل 16. رسم الخرائط',
    'Chapter 17. Widgets and their configuration': 'الفصل 17. الأدوات وتهيئتها',
    'Chapter 18. Notebooks': 'الفصل 18. الدفاتر',
    'Chapter 19. Dashboards': 'الفصل 19. لوحات المعلومات',
    'Chapter 20. Outbreaks': 'الفصل 20. تفشي الأمراض',
    'Chapter 21. Documents and Document Templates': 'الفصل 21. المستندات وقوالب المستندات',
    'Chapter 22. Website Builder': 'الفصل 22. منشئ المواقع الإلكترونية',
    'Chapter 23. Export': 'الفصل 23. التصدير',
    'Chapter 24. SMS reporting and teams': 'الفصل 24. الإبلاغ عبر الرسائل النصية والفرق',
    'Chapter 25. EWARS Stand-alone': 'الفصل 25. EWARS المستقل',
    'Chapter 26. Glossary': 'الفصل 26. المسرد',
    'Chapter 27. Help and support': 'الفصل 27. المساعدة والدعم',
  },
}

BANNER = {
  'fr': ('> **Traduction en cours.** Cette page attend sa traduction française. '
         'La version anglaise fait foi entre-temps — voir '),
  'es': ('> **Traducción en curso.** Esta página está pendiente de traducción al español. '
         'Mientras tanto, la versión en inglés es la referencia — ver '),
  'ar': ('> **الترجمة قيد التنفيذ.** بانتظار ترجمة هذه الصفحة إلى العربية. '
         'يُرجى الرجوع إلى النسخة الإنجليزية في الوقت الحالي — انظر '),
}

LANG_META = {
  'fr': {'label': 'chapitres/', 'book_title': 'EWARS in a Box', 'book_sub': "Guide d'utilisation Web", 'dir': 'ltr'},
  'es': {'label': 'capitulos/', 'book_title': 'EWARS in a Box', 'book_sub': 'Guía de uso web', 'dir': 'ltr'},
  'ar': {'label': 'فصول/', 'book_title': 'EWARS in a Box', 'book_sub': 'دليل استخدام الويب', 'dir': 'rtl'},
}

for lang in ('fr', 'es', 'ar'):
    chdir = f'{lang}/chapters'
    os.makedirs(chdir, exist_ok=True)
    for entry in manifest:
        if entry['type'] != 'chapter':
            continue
        title_en = entry['title']
        title_l = TITLES[lang].get(title_en, title_en)
        fname = os.path.basename(entry['file'])
        en_rel = f"../../en/{entry['file']}"
        content = f"# {title_l}\n\n{BANNER[lang]}[{title_en}]({en_rel}).\n"
        with open(f'{chdir}/{fname}', 'w', encoding='utf-8') as f:
            f.write(content)

print("Scaffolded fr/es/ar chapter placeholders")
