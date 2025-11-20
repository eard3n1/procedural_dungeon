<h1>procedural_dungeon</h1>
<p>A minimal seed-based procedural dungeon generator with a simple CLI.</p>
<img src="example.png" title="Seed" style="width:256px;height:256px;>

<h2>Features</h2>
<ul>
    <li>Deterministic dungeon generation utilizing seed</li>
    <li>Optional ASCII visualization in the terminal</li>
    <li>PNG export: <code>output/dungeon.png</code></li>  
</ul>

<h2>Installation</h2>
<p>This program only depends on <strong>Pillow</strong> for PNG output:</p>
<pre><code>pip install Pillow</code></pre>

<h2>Usage</h2>
<ul>
    <li><p>Default use scenario:</p>
    <pre><code>python main.py</code></pre></li>
    <li><p>Show ASCII output:</p>
    <pre><code>python main.py --ascii</code></pre></li>
    <li><p>Use a specific seed:</p>
    <pre><code>python main.py --seed 67</code></pre></li>
</ul>

<h2>License</h2>
<p>MIT License</p>