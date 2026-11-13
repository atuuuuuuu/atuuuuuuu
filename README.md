<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Usukhbayar (atu), Ulaanbaatar, Mongolia. Curious about how things work, so I build small tools to find out." width="100%">
</picture>

<br>

I'm a 3rd-year student at **New Mongol College of Technology** in Ulaanbaatar. I build small, focused tools for the Mac
and the browser: the kind that do one job well and keep your files and your data on your own device.
I also make music, so I like projects where code and sound meet.

**[Unpacked](#unpacked)** · **[Convrt](#convrt)** · [Other work](#other-work) · [Toolbox](#toolbox)

<br>

## Selected work

<br>

<div align="center">
  <a href="https://atuuuuuuu.github.io/unpacked/"><img src="https://raw.githubusercontent.com/atuuuuuuu/unpacked/main/docs/media/logo.svg" width="56" height="56" alt="Unpacked logo"></a>
  <h3 id="unpacked">Unpacked</h3>
  <p><b>Your data exports, unpacked. Privately.</b><br>
  Drop the ZIP that Spotify, Instagram or YouTube gives you and get clear charts and lists, computed entirely in your browser.</p>
  <a href="https://atuuuuuuu.github.io/unpacked/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/atuuuuuuu/unpacked/main/docs/media/spotify-dark.png">
      <img src="https://raw.githubusercontent.com/atuuuuuuu/unpacked/main/docs/media/spotify-light.png" width="100%" alt="Unpacked Spotify dashboard with sample data: listening time, hours per year and highlights">
    </picture>
  </a>
  <p>
    <a href="https://atuuuuuuu.github.io/unpacked/"><img src="https://img.shields.io/badge/Live_demo-0b7a75?style=for-the-badge" alt="Live demo"></a>
    <a href="https://github.com/atuuuuuuu/unpacked"><img src="https://img.shields.io/badge/Source-24292f?style=for-the-badge&logo=github&logoColor=white" alt="Source on GitHub"></a>
  </p>
</div>

- **Three platforms:** Spotify listening history, Instagram followers (including who unfollowed you, by comparing two
  exports) and YouTube watch history.
- **Nothing leaves your device.** The ZIP is read in a Web Worker, a strict CSP blocks every other site, and an
  end-to-end test fails the build if any request goes out.
- **Works offline** as an installable app, with sample data to try before your export arrives.
- **Share cards:** a 1080×1350 image of your stats, drawn on your device.

<sub><b>Stack</b> &nbsp; TypeScript · React 19 · Vite · Tailwind CSS · Radix · zip.js · Zod · d3 · Vitest · Playwright</sub>

<br><br>

<div align="center">
  <a href="https://github.com/atuuuuuuu/Convrt"><img src="https://raw.githubusercontent.com/atuuuuuuu/Convrt/main/assets/app-icon.png" width="56" height="56" alt="Convrt app icon"></a>
  <h3 id="convrt">Convrt</h3>
  <p><b>Drag a file. Hold Shift. Drop it on a slice.</b><br>
  A macOS menu bar app that opens a wheel of formats and tools right at your cursor. Fully offline, no account.</p>
  <a href="https://github.com/atuuuuuuu/Convrt">
    <img src="https://raw.githubusercontent.com/atuuuuuuu/Convrt/main/assets/wheels.png" width="100%" alt="Convrt's three wheels: Convert, Tools and Actions">
  </a>
  <p>
    <a href="https://github.com/atuuuuuuu/Convrt/releases/latest"><img src="https://img.shields.io/badge/Download_v1.0-2f6fe0?style=for-the-badge&logo=apple&logoColor=white" alt="Download Convrt"></a>
    <a href="https://github.com/atuuuuuuu/Convrt"><img src="https://img.shields.io/badge/Source-24292f?style=for-the-badge&logo=github&logoColor=white" alt="Source on GitHub"></a>
  </p>
</div>

- **Convert** images, audio, video and PDFs. The wheel only shows what fits the files you're dragging.
- **Tools** like compress, resize, strip EXIF and GPS, cut out the background, trim video and merge PDFs.
- **Beyond the wheel:** a Drop Zone window, a floating shelf, watch folders and a `convrt` command-line tool on the
  same engine.
- **Safe by default:** results land next to the originals, nothing is overwritten, and there is no network code at all.

<sub><b>Stack</b> &nbsp; Swift · SwiftUI · AppKit · AVFoundation · PDFKit · Vision · GitHub Actions</sub>

<br><br>

## Other work

**Earth Jukebox** &nbsp;<sub>NASA Space Apps 2026 · private for now</sub><br>
NASA sea surface temperature maps turned into music in the browser: warmer water sounds higher, the ocean sweeps from
your left ear to your right, and a WebGL globe shows what's playing. Built to work with a keyboard and a screen reader.

**[AI ChatAssistant](https://github.com/atuuuuuuu/AI-ChatAssistant)** &nbsp;<sub>school project</sub><br>
A voice-controlled Chrome extension that searches, navigates and describes web pages with on-device Gemini Nano.

**Learning projects** &nbsp;<sub>one file each, built to learn from</sub><br>
[study-timer](https://github.com/atuuuuuuu/study-timer) (a focus timer) ·
[budget-tracker](https://github.com/atuuuuuuu/budget-tracker) (a family budget) ·
[photo-renamer](https://github.com/atuuuuuuu/photo-renamer) (renames photos by date)

<br>

## Toolbox

<a href="#toolbox"><img src="https://skillicons.dev/icons?i=swift,apple,ts,js,react,vite,tailwind,py,cpp,html,css,nodejs,electron,githubactions,git&perline=15" alt="Swift, macOS, TypeScript, JavaScript, React, Vite, Tailwind CSS, Python, C++, HTML, CSS, Node.js, Electron, GitHub Actions, Git" width="600"></a>

Right now I'm learning more **Swift**, **WebGL** and **audio programming**.

<br>

<div align="center">
  <sub>Found a bug or have an idea? Open an issue on any of my repos.</sub>
</div>
