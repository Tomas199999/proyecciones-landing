# -*- coding: utf-8 -*-
"""Genera las cuatro páginas legales de la landing.

Se corre a mano cuando hay que regenerarlas; el resultado se commitea. El
proyecto no tiene build y no conviene que lo tenga por esto.
"""

import io
import os

DIR = '/Users/tomasfederico/projects/proyecciones-landing'
MAIL = 'hola@ejemplo.com'          # TODO: el mail real, antes de publicar
FECHA = '2 de octubre de 2026'

SHELL = u'''<!DOCTYPE html>
<html lang="es-AR" class="scroll-smooth">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Atino</title>
<meta name="description" content="{desc}">

<!-- Evita el parpadeo de tema antes de pintar -->
<script>
  (function () {{
    try {{
      var t = localStorage.getItem('tema');
      if (t === 'oscuro' || (!t && matchMedia('(prefers-color-scheme: dark)').matches)) {{
        document.documentElement.classList.add('dark');
      }}
    }} catch (e) {{}}
  }})();
</script>

<script src="https://cdn.tailwindcss.com"></script>
<script src="/assets/base.js"></script>

<style>
  body {{ -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }}

  /* Tipografía del documento: un solo lugar para todo el cuerpo legal. */
  .doc h2 {{ font-family: ui-serif, Charter, 'Iowan Old Style', Georgia, serif;
             font-size: 1.35rem; font-weight: 600; letter-spacing: -.01em; margin-top: 2.75rem; }}
  .doc h3 {{ font-size: 1rem; font-weight: 600; margin-top: 1.75rem; }}
  .doc p, .doc li {{ font-size: 15px; line-height: 1.7; }}
  .doc p {{ margin-top: .9rem; color: #5B5D64; }}
  .dark .doc p {{ color: #95989E; }}
  .doc ul, .doc ol {{ margin-top: .9rem; padding-left: 1.15rem; color: #5B5D64; }}
  .dark .doc ul, .dark .doc ol {{ color: #95989E; }}
  .doc ul {{ list-style: disc; }}
  .doc ol {{ list-style: decimal; }}
  .doc li {{ margin-top: .45rem; padding-left: .2rem; }}
  .doc li::marker {{ color: #D6D1C5; }}
  .dark .doc li::marker {{ color: #343941; }}
  .doc strong {{ color: #15161A; font-weight: 600; }}
  .dark .doc strong {{ color: #EBEBE6; }}
  .doc code {{ font-size: 13px; }}
</style>
</head>

<body class="bg-paper text-ink dark:bg-night dark:text-bone font-sans antialiased">

<header class="sticky top-0 z-50 px-4 pt-4">
  <nav class="mx-auto flex max-w-content items-center justify-between gap-4 rounded-xl border border-line bg-card/85 px-4 py-2.5 backdrop-blur-md dark:border-edge dark:bg-panel/85">
    <a href="/" class="flex items-center gap-2.5">
      <span class="grid h-7 w-7 place-items-center rounded-md border border-line2 bg-paper dark:border-edge2 dark:bg-night">
        <svg viewBox="0 0 16 16" class="h-4 w-4" aria-hidden="true">
          <path d="M2 12.5 5.4 9.1l2.4 1.6L13.4 4.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="text-bien dark:text-bien2"/>
          <circle cx="13.4" cy="4.2" r="1.5" fill="currentColor" class="text-bien dark:text-bien2"/>
        </svg>
      </span>
      <span class="font-display text-[17px] font-semibold tracking-tight">Atino</span>
    </a>

    <div class="flex items-center gap-2">
      <a href="/" class="rounded-lg px-3 py-2 text-[13px] text-soft transition hover:text-ink dark:text-bonesoft dark:hover:text-bone">Volver</a>
      <button id="btn-tema" type="button" aria-label="Cambiar tema"
        class="grid h-9 w-9 place-items-center rounded-lg border border-line text-soft transition hover:bg-paper dark:border-edge dark:text-bonesoft dark:hover:bg-night">
        <svg class="h-4 w-4 dark:hidden" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <path d="M16 11.5A6.5 6.5 0 0 1 8.5 4a6.5 6.5 0 1 0 7.5 7.5Z" stroke-linejoin="round"/>
        </svg>
        <svg class="hidden h-4 w-4 dark:block" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <circle cx="10" cy="10" r="3.6"/>
          <path d="M10 1.6v2M10 16.4v2M1.6 10h2M16.4 10h2M4.1 4.1l1.4 1.4M14.5 14.5l1.4 1.4M15.9 4.1l-1.4 1.4M5.5 14.5l-1.4 1.4" stroke-linecap="round"/>
        </svg>
      </button>
    </div>
  </nav>
</header>

<main class="px-4 py-14 sm:py-20">
  <article class="doc mx-auto max-w-[46rem]">
    <p class="font-mono text-[11px] uppercase tracking-[0.16em] text-soft dark:text-bonesoft">{kicker}</p>
    <h1 class="mt-3 font-display text-3xl font-semibold tracking-tight sm:text-[2.3rem] sm:leading-[1.14]">{h1}</h1>
    <p class="mt-5 text-[16px] leading-relaxed text-soft dark:text-bonesoft">{lead}</p>
    <p class="mt-6 font-mono text-[11px] text-soft dark:text-bonesoft">Última actualización: {fecha}</p>

    <div class="mt-10 border-t border-line pt-2 dark:border-edge">
{body}
    </div>

    <nav class="mt-16 grid gap-2 rounded-xl border border-line bg-card p-5 dark:border-edge dark:bg-panel sm:grid-cols-2" aria-label="Otros documentos">
      <p class="font-mono text-[11px] uppercase tracking-[0.14em] text-soft dark:text-bonesoft sm:col-span-2">Los otros tres</p>
      {hermanas}
    </nav>

    <div class="mt-4 rounded-xl border border-line bg-card p-5 dark:border-edge dark:bg-panel">
      <p class="text-[14px] font-medium">¿Algo de esto no te cierra?</p>
      <p class="mt-1.5 text-[13px] leading-relaxed text-soft dark:text-bonesoft">
        Escribinos y lo revisamos con vos antes de firmar. Si tu abogado quiere otra redacción,
        se negocia: esto es el piso, no un decreto.
      </p>
      <a href="mailto:{mail}" class="mt-3 inline-block font-mono text-[12px] text-bien underline underline-offset-4 dark:text-bien2">{mail}</a>
    </div>
  </article>
</main>

<footer class="border-t border-line px-4 py-12 dark:border-edge">
  <div class="mx-auto flex max-w-content flex-col gap-8 sm:flex-row sm:items-start sm:justify-between">
    <div>
      <p class="font-display text-[17px] font-semibold tracking-tight">Atino</p>
      <p class="mt-2 max-w-xs text-[14px] leading-relaxed text-soft dark:text-bonesoft">
        Sistema de soporte a decisiones para empresas que ya generan datos y todavía no los usan.
      </p>
      <p class="mt-4 font-mono text-[11px] text-soft dark:text-bonesoft">Buenos Aires, Argentina</p>
    </div>

    <div class="grid grid-cols-2 gap-x-12 gap-y-2 text-[14px] sm:gap-x-16">
      <a href="/privacidad" class="{c_priv} transition hover:text-ink dark:hover:text-bone">Privacidad</a>
      <a href="/seguridad" class="{c_seg} transition hover:text-ink dark:hover:text-bone">Seguridad</a>
      <a href="/terminos" class="{c_ter} transition hover:text-ink dark:hover:text-bone">Términos</a>
      <a href="/tratamiento-de-datos" class="{c_tra} transition hover:text-ink dark:hover:text-bone">Tratamiento de datos</a>
      <a href="/#faq" class="text-soft transition hover:text-ink dark:text-bonesoft dark:hover:text-bone">Preguntas</a>
      <a href="mailto:{mail}" class="text-soft transition hover:text-ink dark:text-bonesoft dark:hover:text-bone">Contacto</a>
    </div>
  </div>
</footer>

</body>
</html>
'''

ACTIVO = 'font-medium text-ink dark:text-bone'
INACTIVO = 'text-soft dark:text-bonesoft'

TITULOS = {
    'privacidad': 'Privacidad',
    'seguridad': 'Seguridad',
    'terminos': 'Términos',
    'tratamiento-de-datos': 'Tratamiento de datos',
}

PAGS = {}

# ─────────────────────────── PRIVACIDAD ───────────────────────────
PAGS['privacidad'] = dict(
    title=u'Privacidad',
    kicker=u'Política de privacidad',
    h1=u'Qué hacemos con los datos personales',
    desc=u'Política de privacidad de Atino: qué datos personales tratamos, para qué, con quién los compartimos y cómo ejercés tus derechos bajo la Ley 25.326.',
    lead=u'Este documento explica qué datos personales trata Atino, con qué finalidad y durante cuánto tiempo. Está escrito para que se entienda, no para cubrirnos.',
    body=u'''
<h2>1. Quién es responsable</h2>
<p>
  Atino opera desde Buenos Aires, Argentina. Para cualquier cuestión sobre este documento o
  sobre tus datos personales, el canal es
  <a href="mailto:{mail}" class="text-bien underline underline-offset-4 dark:text-bien2">{mail}</a>,
  y contestamos en el día.
</p>
<!-- TODO: razón social, CUIT y domicilio legal cuando esté constituida la sociedad -->

<h2>2. Dos situaciones distintas</h2>
<p>Conviene separarlas desde el principio, porque las reglas no son las mismas:</p>
<ul>
  <li>
    <strong>Visitás este sitio o nos escribís.</strong> Ahí tratamos tus datos como responsables:
    decidimos nosotros qué se hace con ellos, y esta política los cubre por completo.
  </li>
  <li>
    <strong>Sos cliente y la plataforma procesa datos de tu empresa.</strong> Ahí el responsable
    sos vos y nosotros somos encargados del tratamiento: hacemos lo que vos nos instruís y nada
    más. Las condiciones están en
    <a href="/tratamiento-de-datos" class="text-bien underline underline-offset-4 dark:text-bien2">Tratamiento de datos</a>.
  </li>
</ul>

<h2>3. Qué datos tratamos</h2>
<h3>Si nos escribís</h3>
<p>
  Tu dirección de correo, tu nombre, la empresa en la que trabajás y lo que nos cuentes en el
  mensaje. Nada de eso lo pedimos por formulario: llega porque vos lo escribiste en un mail.
</p>
<h3>Si avanzamos a un diagnóstico</h3>
<p>
  Datos de contacto de las personas de tu equipo con las que coordinamos, y la información de
  negocio que decidas compartir para que evaluemos si tus datos alcanzan. Si en esa muestra hay
  datos personales de terceros —clientes tuyos, por ejemplo— te vamos a pedir que los anonimices
  antes de mandarlos, y si no se puede, firmamos el acuerdo de tratamiento primero.
</p>
<h3>Si navegás este sitio</h3>
<p>
  <strong>No usamos cookies, ni analítica, ni píxeles de seguimiento.</strong> No hay Google
  Analytics, no hay Meta Pixel, no hay nada que te siga entre sitios. Lo único que se guarda en
  tu navegador es una preferencia llamada <code>tema</code>, en <code>localStorage</code>, para
  recordar si elegiste modo claro u oscuro. Vive en tu equipo, no viaja a ningún servidor y la
  borrás limpiando los datos del sitio.
</p>
<p>
  El sitio sí carga una hoja de estilos desde <code>cdn.tailwindcss.com</code>. Esa petición deja
  tu dirección IP en los registros de ese proveedor, como cualquier recurso externo de cualquier
  página. No le mandamos ningún dato tuyo nosotros.
</p>

<h2>4. Para qué los usamos</h2>
<ul>
  <li>Contestarte, coordinar una reunión y prepararte una propuesta.</li>
  <li>Prestar el servicio contratado y sostenerlo mes a mes.</li>
  <li>Cumplir obligaciones legales, impositivas y contables.</li>
</ul>
<p>
  No hacemos perfilado publicitario, no vendemos ni cedemos bases de datos, y no te vamos a
  mandar newsletters que no pediste.
</p>

<h2>5. Con quién los compartimos</h2>
<p>
  Con los proveedores de infraestructura y de correo necesarios para que esto funcione, y nada
  más. No hay intermediarios comerciales ni brokers de datos en el medio. Si sos cliente, la
  lista concreta de proveedores que tocan tu instancia va nombrada en el contrato, con nombre y
  país, y te avisamos antes de cambiarla.
</p>
<p>
  Algunos de esos proveedores están fuera de la Argentina. Cuando eso implica una transferencia
  internacional, se hace con las garantías que exige la normativa vigente.
</p>
<!-- TODO: nombrar los proveedores concretos (infraestructura, correo) y sus países -->

<h2>6. Cuánto tiempo los guardamos</h2>
<ul>
  <li><strong>Consultas que no avanzan:</strong> hasta dos años, por si retomás la conversación.</li>
  <li><strong>Datos de clientes:</strong> mientras dure el contrato, más los plazos legales de conservación fiscal y contable.</li>
  <li><strong>Datos de negocio procesados en tu instancia:</strong> lo que diga el acuerdo de tratamiento; al terminar, se devuelven o se borran, como elijas.</li>
</ul>

<h2>7. Tus derechos</h2>
<p>
  Podés pedir acceso, rectificación, actualización y supresión de tus datos personales, en los
  términos de la <strong>Ley 25.326 de Protección de los Datos Personales</strong>. Escribís a
  <a href="mailto:{mail}" class="text-bien underline underline-offset-4 dark:text-bien2">{mail}</a>
  y te contestamos: el acceso dentro de los diez días corridos, la rectificación o supresión
  dentro de los cinco días hábiles de acreditada la solicitud.
</p>
<p>
  La <strong>Agencia de Acceso a la Información Pública</strong> es el órgano de control de esa
  ley y tiene atribuciones para atender las denuncias de quien considere afectados sus derechos.
</p>

<h2>8. Menores de edad</h2>
<p>
  Esto es un servicio para empresas. No está dirigido a menores de 18 años y no recolectamos sus
  datos a sabiendas.
</p>

<h2>9. Cambios</h2>
<p>
  Si cambiamos algo de fondo, cambia la fecha de arriba y, si sos cliente, te lo avisamos por
  mail antes de que aplique. No modificamos esta política en silencio.
</p>
''')

# ─────────────────────────── SEGURIDAD ───────────────────────────
PAGS['seguridad'] = dict(
    title=u'Seguridad',
    kicker=u'Seguridad de la información',
    h1=u'Cómo protegemos lo que nos confiás',
    desc=u'Cómo aísla Atino los datos de cada cliente, cómo los cifra, quién accede, qué queda auditado y cómo reportar una vulnerabilidad.',
    lead=u'Lo que sigue son compromisos que podés auditar y, si hace falta, escribir en el contrato. Si algo acá no se corresponde con lo que ves en la plataforma, es un error nuestro y queremos saberlo.',
    body=u'''
<h2>1. Cada cliente, su propia instancia</h2>
<p>
  No hay una base compartida con los datos de todos. Cada cliente corre en su instancia, con su
  base separada. Esa es la razón por la que podemos afirmar que tus datos no se mezclan con los
  de otro: no es una política de acceso, es una separación de infraestructura.
</p>

<h2>2. Cifrado</h2>
<p>
  Los datos van cifrados en tránsito y en reposo. La plataforma se sirve exclusivamente por HTTPS.
</p>

<h2>3. Quién accede, y qué queda registrado</h2>
<ul>
  <li>
    <strong>De tu lado:</strong> los accesos son nominales —una persona, un usuario— y con
    permisos por rol. Compras ve stock, Cobranzas ve mora, la dirección ve el conjunto.
  </li>
  <li>
    <strong>De nuestro lado:</strong> acceden únicamente las personas asignadas a tu cuenta, y
    solo para tareas de operación y soporte.
  </li>
  <li>
    <strong>En los dos casos:</strong> queda registro de quién miró qué y cuándo. Ese registro es
    auditable y te lo podemos exportar cuando lo pidas.
  </li>
</ul>

<h2>4. Tus datos no entrenan modelos de otros</h2>
<p>
  Lo que se comparte entre clientes es el código de la plataforma: los conectores, los tipos de
  modelo, la lógica de alertas. Tus datos, y los modelos entrenados con tus datos, son tuyos y no
  salen de tu instancia. Va escrito en el contrato, no es una promesa de landing.
</p>

<h2>5. Si tu política interna lo exige, va en tu propia nube</h2>
<p>
  La plataforma se puede desplegar en tu infraestructura o en tu cuenta de nube. En ese escenario
  el control de acceso lo tenés vos entero y nosotros entramos solo cuando nos habilitás. El
  precio cambia; la funcionalidad, no.
</p>

<h2>6. Accesos a tus sistemas</h2>
<p>
  Para conectar el ERP pedimos siempre el <strong>mínimo privilegio</strong>: acceso de lectura,
  sobre las tablas o los endpoints que hacen falta, con credenciales propias nuestras y revocables
  por vos en cualquier momento. Nunca pedimos una credencial de administrador compartida, y si
  alguien de nuestro lado te la pide, no se la des y escribinos.
</p>

<h2>7. Si pasa algo</h2>
<p>
  Si detectamos un incidente de seguridad que afecte tus datos, te avisamos sin demora indebida,
  con lo que sepamos hasta ese momento: qué pasó, qué datos están comprometidos, qué estamos
  haciendo y qué te conviene hacer a vos. Después mandamos el informe completo. Preferimos avisar
  temprano con información incompleta que tarde con el relato ordenado.
</p>
<!-- TODO: si algún contrato exige un plazo máximo de notificación (24 h, 72 h), fijarlo acá también -->

<h2>8. Reportar una vulnerabilidad</h2>
<p>
  Si encontraste algo, escribinos a
  <a href="mailto:{mail}?subject=Reporte%20de%20seguridad" class="text-bien underline underline-offset-4 dark:text-bien2">{mail}</a>
  con el asunto «Reporte de seguridad». Te contestamos dentro de las 72 horas. No tenemos
  programa de recompensas, pero no iniciamos acciones legales contra quien investiga de buena fe,
  sin degradar el servicio, sin acceder a datos de terceros y sin publicar antes de que lo
  hayamos corregido.
</p>

<h2>9. Lo que todavía no tenemos</h2>
<p>
  No tenemos certificación ISO 27001 ni informe SOC 2. Si tu área de compliance los exige como
  requisito, hoy no los cumplimos y preferimos decirlo acá antes que en la última reunión. Lo que
  sí hacemos es responder cuestionarios de seguridad y aceptar las cláusulas que tu equipo
  necesite.
</p>
''')

# ─────────────────────────── TÉRMINOS ───────────────────────────
PAGS['terminos'] = dict(
    title=u'Términos',
    kicker=u'Términos y condiciones',
    h1=u'Las reglas del servicio',
    desc=u'Términos y condiciones del servicio de Atino: alcance, precios, propiedad de los datos y los modelos, límites de responsabilidad, baja y jurisdicción.',
    lead=u'Estas condiciones generales aplican al servicio de Atino. Lo particular de cada cliente —alcance, precio y plazos— va en la propuesta firmada, que prevalece sobre este texto cuando difieren.',
    body=u'''
<h2>1. Qué contratás</h2>
<p>Dos cosas, y conviene no confundirlas:</p>
<ol>
  <li>
    <strong>Una implementación inicial:</strong> conectar tus sistemas, ordenar los datos, montar
    los dashboards y poner a andar los primeros modelos. Tiene alcance y plazo definidos en la
    propuesta.
  </li>
  <li>
    <strong>Un abono mensual:</strong> que la plataforma siga andando, los modelos se sigan
    midiendo contra la realidad y se corrijan cuando se degradan. No es soporte pasivo: es
    mantener vivo algo que se degrada solo.
  </li>
</ol>
<p>
  El servicio es para empresas. Quien contrata declara que lo hace en nombre de una persona
  jurídica y que tiene facultades para obligarla.
</p>

<h2>2. Precio y facturación</h2>
<p>
  El precio de la implementación y el del abono son los de la propuesta que hayas firmado. El
  abono se factura por mes adelantado. Si actualizamos el abono, te avisamos con 60 días de
  anticipación y podés dar de baja sin penalidad antes de que aplique.
</p>

<h2>3. De quién es cada cosa</h2>
<ul>
  <li>
    <strong>Tuyos:</strong> tus datos, y los modelos entrenados con tus datos. Si te vas, te los
    llevás.
  </li>
  <li>
    <strong>Nuestra:</strong> la plataforma —el código, los conectores, los tipos de modelo, la
    lógica de alertas, el diseño—. Contratás el derecho a usarla mientras dure el contrato, no la
    propiedad.
  </li>
  <li>
    <strong>Aprendizaje genérico:</strong> lo que aprendemos haciendo tu implementación, a nivel
    de cómo se resuelve un problema, lo seguimos usando. Lo que no se usa ni se transfiere es tu
    información.
  </li>
</ul>

<h2>4. Lo que el servicio no es</h2>
<p>
  Atino es una herramienta de <strong>soporte a la decisión</strong>. Las proyecciones y las
  alertas son estimaciones con error medido, no certezas: cada número va con su banda y con la
  precisión de los últimos meses a la vista. <strong>La decisión de negocio es siempre tuya</strong>,
  y quien conoce la operación tiene que poder desoír al modelo.
</p>
<p>
  No damos asesoramiento financiero, contable, impositivo ni legal, y el servicio no reemplaza
  los controles internos de tu empresa.
</p>

<h2>5. Confidencialidad</h2>
<p>
  Todo lo que veamos de tu operación es confidencial y no se comparte con nadie fuera del equipo
  asignado a tu cuenta. La obligación sigue vigente después de terminado el contrato. Si querés
  nombrarte como caso o logo en nuestro sitio, te lo pedimos por escrito y podés decir que no sin
  que eso cambie nada del servicio.
</p>

<h2>6. Disponibilidad</h2>
<p>
  Hacemos mantenimiento programado avisando con anticipación y, cuando se puede, fuera del
  horario de operación. Si tu caso necesita un compromiso de disponibilidad con número y
  consecuencia, se acuerda por escrito en la propuesta; sin eso firmado, no hay SLA garantizado.
</p>

<h2>7. Responsabilidad</h2>
<p>
  Respondemos por los daños directos que causemos por incumplimiento, con el límite de lo que nos
  hayas pagado en los doce meses anteriores al hecho. No respondemos por lucro cesante ni por
  decisiones de negocio tomadas a partir de una proyección. Nada de esto limita la responsabilidad
  por dolo o culpa grave, ni los derechos que la normativa de orden público te reconozca.
</p>

<h2>8. Dar de baja</h2>
<p>
  Podés dar de baja el abono avisando con 30 días. No hay penalidad ni permanencia mínima más
  allá de lo que figure en la propuesta. Al terminar:
</p>
<ul>
  <li>Te exportamos tus datos y tus modelos en formato utilizable, sin cobrar por eso.</li>
  <li>Tenés 30 días para pedir esa exportación.</li>
  <li>Pasado ese plazo, damos de baja la instancia y borramos los datos, salvo lo que debamos conservar por ley.</li>
</ul>
<p>
  Podemos suspender el servicio por falta de pago, avisando antes y dándote plazo para regularizar.
</p>

<h2>9. Cambios en estas condiciones</h2>
<p>
  Si las modificamos, cambia la fecha de arriba y te avisamos por mail con 30 días de
  anticipación. Si el cambio no te sirve, podés dar de baja sin penalidad dentro de ese plazo.
</p>

<h2>10. Ley aplicable</h2>
<p>
  Se aplica la ley argentina. Cualquier controversia se somete a los tribunales ordinarios de la
  Ciudad Autónoma de Buenos Aires, salvo que la propuesta firmada indique otra cosa.
</p>
<!-- TODO: confirmar jurisdicción con el abogado antes de publicar en serio -->
''')

# ─────────────────── TRATAMIENTO DE DATOS ───────────────────
PAGS['tratamiento-de-datos'] = dict(
    title=u'Tratamiento de datos',
    kicker=u'Acuerdo de tratamiento de datos',
    h1=u'Qué hacemos con los datos de tu empresa',
    desc=u'Condiciones bajo las que Atino trata, como encargado, los datos personales contenidos en los sistemas de sus clientes: finalidad, instrucciones, subencargados, incidentes y devolución.',
    lead=u'Cuando la plataforma procesa los datos de tu empresa, el responsable del tratamiento sos vos y nosotros somos el encargado. Este documento fija qué podemos y qué no podemos hacer con ellos.',
    body=u'''
<h2>1. Los roles</h2>
<p>
  En los términos de la <strong>Ley 25.326</strong>, vos sos el <strong>responsable</strong>: los
  datos son de tu empresa y las decisiones sobre ellos son tuyas. Atino es el
  <strong>encargado</strong>: los tratamos por cuenta tuya, únicamente para prestarte el servicio,
  y siguiendo tus instrucciones.
</p>
<p>
  Si nos das una instrucción que entendemos contraria a la normativa, te lo decimos por escrito
  antes de ejecutarla.
</p>

<h2>2. Objeto, duración y finalidad</h2>
<ul>
  <li><strong>Objeto:</strong> alojar y procesar los datos de tus sistemas para generar dashboards, predicciones y alertas.</li>
  <li><strong>Duración:</strong> la del contrato de servicio, más el plazo de devolución del punto 8.</li>
  <li><strong>Finalidad:</strong> prestarte el servicio. Ninguna otra. No usamos tus datos para desarrollar productos, entrenar modelos de otros clientes, ni construir bases agregadas.</li>
</ul>

<h2>3. Qué datos entran</h2>
<p>
  Los que traigan tus sistemas: ventas, stock, cobranzas, clientes, proveedores. Típicamente
  incluyen datos identificatorios y comerciales de tus clientes y contactos —nombre, razón social,
  CUIT, domicilio, historial de compra y de pago— y datos de las personas de tu equipo que usan la
  plataforma.
</p>
<p>
  <strong>No queremos datos sensibles.</strong> Salud, origen racial o étnico, opiniones políticas,
  convicciones religiosas, afiliación sindical o vida sexual, en los términos del artículo 2 de la
  Ley 25.326, no deben entrar a la plataforma. Si tu operación los incluye necesariamente, hay que
  acordarlo por escrito antes de conectar nada.
</p>

<h2>4. Nuestras obligaciones</h2>
<ul>
  <li>Tratar los datos solo para la finalidad del punto 2 y según tus instrucciones.</li>
  <li>Mantener la confidencialidad, también después de terminado el contrato.</li>
  <li>Obligar a la confidencialidad a toda persona de nuestro equipo con acceso.</li>
  <li>Aplicar las medidas de seguridad descritas en <a href="/seguridad" class="text-bien underline underline-offset-4 dark:text-bien2">Seguridad</a>.</li>
  <li>Limitar el acceso a las personas asignadas a tu cuenta y dejar registro auditable de los accesos.</li>
  <li>No transferir ni ceder los datos a terceros fuera de lo previsto en el punto 5.</li>
</ul>

<h2>5. Subencargados</h2>
<p>
  Para prestar el servicio usamos proveedores de infraestructura y de correo. Son subencargados, y
  quedan obligados por escrito a las mismas condiciones que asumimos nosotros. La lista vigente,
  con nombre, función y país, va nombrada en tu contrato.
</p>
<p>
  Si cambiamos o sumamos alguno, te avisamos con anticipación razonable y podés objetarlo. Si el
  cambio te resulta inaceptable y no encontramos alternativa, podés dar de baja sin penalidad.
</p>
<!-- TODO: mantener la lista de subencargados como anexo del contrato, con nombre y país -->

<h2>6. Derechos de los titulares</h2>
<p>
  Si un cliente tuyo ejerce su derecho de acceso, rectificación o supresión, quien tiene que
  responderle sos vos. Nosotros te asistimos: te damos las herramientas para localizar, exportar,
  corregir o borrar esos datos dentro de la plataforma, y si el pedido nos llega directamente a
  nosotros, te lo derivamos en lugar de contestarlo por nuestra cuenta.
</p>

<h2>7. Incidentes</h2>
<p>
  Si tomamos conocimiento de un incidente de seguridad que afecte tus datos, te notificamos sin
  demora indebida y te damos la información que tengamos para que puedas cumplir con tus propias
  obligaciones de notificación. También colaboramos con la investigación y con la remediación.
</p>

<h2>8. Devolución y borrado</h2>
<p>
  Al terminar el contrato, elegís vos: te devolvemos los datos y los modelos en formato utilizable,
  o los borramos. Tenés 30 días para decidirlo y para bajar la exportación. Pasado ese plazo,
  borramos la instancia y todas sus copias, salvo lo que debamos conservar por una obligación
  legal —y en ese caso te decimos qué queda, por qué y hasta cuándo—.
</p>

<h2>9. Auditoría</h2>
<p>
  Podés pedirnos la información razonable para verificar que cumplimos con esto, y responder
  cuestionarios de seguridad de tu área de compliance. Si tu política exige una auditoría en sitio,
  se coordina con anticipación, sin interrumpir la operación y sin exponer datos de otros clientes.
</p>

<h2>10. Prevalece el contrato firmado</h2>
<p>
  Si firmamos un acuerdo de tratamiento de datos particular con tu empresa, ese texto prevalece
  sobre este. Lo de acá es el piso que aplica a falta de uno.
</p>
''')


def hermanas_de(slug):
    filas = []
    for otro, titulo in TITULOS.items():
        if otro == slug:
            continue
        filas.append(
            u'<a href="/%s" class="rounded-lg border border-line px-4 py-3 text-[14px] transition '
            u'hover:border-line2 hover:bg-paper dark:border-edge dark:hover:border-edge2 dark:hover:bg-night">%s</a>'
            % (otro, titulo)
        )
    return u'\n      '.join(filas)


for slug, d in PAGS.items():
    body = d['body'].format(mail=MAIL)
    html = SHELL.format(
        title=d['title'], desc=d['desc'], kicker=d['kicker'], h1=d['h1'],
        lead=d['lead'], body=body, fecha=FECHA, mail=MAIL,
        hermanas=hermanas_de(slug),
        c_priv=ACTIVO if slug == 'privacidad' else INACTIVO,
        c_seg=ACTIVO if slug == 'seguridad' else INACTIVO,
        c_ter=ACTIVO if slug == 'terminos' else INACTIVO,
        c_tra=ACTIVO if slug == 'tratamiento-de-datos' else INACTIVO,
    )
    io.open(os.path.join(DIR, slug + '.html'), 'w', encoding='utf-8').write(html)
    print('escrito', slug + '.html', len(html), 'bytes')
