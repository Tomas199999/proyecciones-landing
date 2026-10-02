/* Configuración compartida por las páginas legales.

   index.html lleva la suya en línea porque es de una sola pieza y sin build;
   acá hay cuatro páginas, y repetir el bloque cuatro veces garantiza que un día
   se desincronicen. Se carga después del CDN de Tailwind y antes de pintar. */

tailwind.config = {
    darkMode: 'class',
    theme: {
      extend: {
        colors: {
          paper:  '#FAF9F5',
          card:   '#FFFFFF',
          line:   '#E5E1D8',
          line2:  '#D6D1C5',
          ink:    '#15161A',
          soft:   '#5B5D64',
          night:  '#0C0D0F',
          panel:  '#141619',
          edge:   '#262A2F',
          edge2:  '#343941',
          bone:   '#EBEBE6',
          bonesoft:'#95989E',
          /* Paleta de estado — validada con scripts/validate_palette.js
             claro: 5/6 PASS (CVD 6,7 = banda piso, legal con etiqueta de texto)
             oscuro: 6/6 PASS */
          bien:   '#0A7550',  bien2:  '#22AC7B',
          aviso:  '#9C6B05',  aviso2: '#B28C04',
          grave:  '#A8272E',  grave2: '#DE5580'
        },
        fontFamily: {
          display: ['ui-serif','Charter','Iowan Old Style','Source Serif 4','Palatino Linotype','Palatino','Georgia','serif'],
          sans: ['system-ui','-apple-system','Segoe UI','Roboto','Helvetica Neue','Arial','sans-serif'],
          mono: ['ui-monospace','SFMono-Regular','SF Mono','Menlo','Consolas','Liberation Mono','monospace']
        },
        maxWidth: { content: '72rem' }
      }
    }
  };

document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('btn-tema');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var oscuro = document.documentElement.classList.toggle('dark');
    try { localStorage.setItem('tema', oscuro ? 'oscuro' : 'claro'); } catch (e) {}
  });
});
