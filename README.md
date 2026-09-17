# Atino — landing

Landing de una sola página para **Atino**, un sistema de soporte a decisiones
(DSS) para empresas: dashboards sobre los datos que ya generan, modelos que predicen
demanda, mora, churn y quiebres de stock, y alertas con la acción recomendada.

Modelo de negocio: implementación inicial + abono mensual.

## Cómo está hecho

Un solo archivo, `index.html`. Sin build, sin dependencias que instalar.

- Tailwind por CDN (`cdn.tailwindcss.com`), configurado en línea
- Modo claro y oscuro, con preferencia guardada en `localStorage`
- Tipografías del sistema: serif para títulos, sans para cuerpo, mono para datos
- El gráfico es SVG escrito a mano, con crosshair y tooltip en JS sin librerías
- Revelado al hacer scroll con `IntersectionObserver`

La paleta de estado (bien / aviso / crítico) está validada para daltonismo y
contraste en ambos modos. Los valores están comentados en el bloque de
configuración de Tailwind; si los tocás, revalidá.

## Correrlo

No hace falta servidor, pero si querés uno:

```sh
python3 -m http.server 4321 --bind 127.0.0.1
# → http://localhost:4321
```

## Deploy

```sh
vercel deploy --prod
```

Producción: https://proyecciones-landing.vercel.app
Demo del dashboard (linkeado desde la landing): https://proyecciones-demo.vercel.app

## Pendientes antes de publicarla en serio

Están marcados con `TODO` en el HTML:

- Precios de implementación y abono (hoy dicen "pago único" y "mensual", sin número)
- Evaluar reemplazar el `mailto:` por un formulario real
- Confirmar los plazos del hero: "diagnóstico sin costo", "6 a 10 semanas"
- Las rutas `/privacidad`, `/seguridad`, `/terminos` y `/tratamiento-de-datos`
  del pie todavía no existen
