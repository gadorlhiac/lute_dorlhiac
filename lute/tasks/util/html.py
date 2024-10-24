"""Utilities for Tasks working with HTML.

This includes HTML templates and associated functions.
"""

__all__ = []
__author__ = "Gabriel Dorlhiac"

DIMPLE_HTML: str = """
<html lang="en">
    <head>
        <title>dimple_thaum - UglyMol</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, user-scalable=no" />
        <meta name="theme-color" content="#333333" />
        <style>
            body {
                font-family: sans-serif;
            }
            canvas {
                display: block;
            }
            #viewer {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
            }
            #hud {
                font-size: 15px;
                color: #ddd;
                background-color: rgba(0, 0, 0, 0.6);
                text-align: center;
                position: absolute;
                top: 10px;
                left: 50%;
                transform: translateX(-50%);
                padding: 2px 8px;
                border-radius: 5px;
                z-index: 9;
                white-space: pre-line;
            }
            #hud u {
                padding: 0 8px;
                text-decoration: none;
                border: solid;
                border-width: 1px 0;
            }
            #hud s {
                padding: 0 8px;
                text-decoration: none;
                opacity: 0.5;
            }
            #help {
                display: none;
                font-size: 16px;
                color: #eee;
                background-color: rgba(0, 0, 0, 0.7);
                position: absolute;
                left: 20px;
                top: 50%;
                transform: translateY(-50%);
                cursor: default;
                padding: 5px;
                border-radius: 5px;
                z-index: 9;
                white-space: pre-line;
            }
            #inset {
                width: 200px;
                height: 200px;
                background-color: #888;
                position: absolute;
                right: 0;
                bottom: 0;
                z-index: 2;
                display: none;
            }
            a {
                color: #59c;
            }
        </style>
        <script src="uglymol.js"></script>
        <script src="wasm/mtz.js"></script>
    </head>
    <body style="background-color: black;">
        <div id="viewer">
            <canvas width="1561" height="1" style="width: 1561px; height: 1px;"></canvas>
        </div>
        <header id="hud" onmousedown="event.stopPropagation();" ondblclick="event.stopPropagation();">This is UglyMol not Coot. <a href="#" onclick="V.toggle_help(); return false;">H shows help.</a></header>
        <footer id="help" style="display: none;">
            <b>mouse:</b>
            Left = rotate Middle or Ctrl+Left = pan Right = zoom Ctrl+Right = clipping Ctrl+Shift+Right = roll Wheel = σ level Shift+Wheel = diff map σ
            <b>keyboard:</b>
            H = toggle help S = general style L = ligand style T = water style C = coloring B = bg color E = toggle fog Q = label font +/- = sigma level ]/[ = map radius D/F = clip width &lt;/&gt; = move clip M/N = zoom U = unitcell box Y =
            hydrogens V = inactive models R = center view W = wireframe style I = spin K = rock Home/End = bond width \ = bond caps P = nearest Cα Shift+P = permalink (Shift+)space = next res. Shift+F = full screen &nbsp;
            <a href="https://uglymol.github.io">uglymol</a> 0.7.0
        </footer>
        <div id="inset"></div>
        <script>
            V = new UM.Viewer({ viewer: "viewer", hud: "hud", help: "help" });
            V.load_pdb("final.pdb");
            GemmiMtz().then(function (Module) {
                UM.load_maps_from_mtz(Module, V, "final.mtz", ["FWT", "PHWT", "DELFWT", "PHDELWT"]);
            });
        </script>
    </body>
</html>
"""
"""HTML Template for UglyMol display of dimple results."""
