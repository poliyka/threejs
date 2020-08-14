import Stats from "./Stats.js"
import { OrbitControls, MapControls } from "./OrbitControls.js"

requirejs.config({
    paths: {
        "THREE": "++plone++test.content/js/three",
    }
});


require(["jquery", "THREE"], function($, THREE) {

    class App {
        constructor() {
            this.scene = new THREE.Scene();
            this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            this.renderer = new THREE.WebGLRenderer({ antialias: true });
            this.renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);

            document.getElementById('view-box').appendChild(this.renderer.domElement);

            window.addEventListener('resize', () => this.onWindowResize());

            const textureLoader = new THREE.TextureLoader();
            const boxTexture = textureLoader.load('++plone++test.content/img/box.jpeg')

            const boxGeometry = new THREE.BoxGeometry(4, 4, 4);
            const material = new THREE.MeshBasicMaterial({ map: boxTexture });
            const mesh = new THREE.Mesh(boxGeometry, material);

            mesh.name = 'box'

            this.camera.position.set(0, 0, 10);

            this.scene.add(mesh);

            this.stats = new Stats();
            this.stats.showPanel(0);
            document.getElementById('view-box').appendChild(this.stats.dom);

            this.orbitControls = new OrbitControls(this.camera, this.renderer.domElement)


            this.render();
        }

        onWindowResize() {
            this.renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);
        }

        render() {
            this.stats.begin();
            window.requestAnimationFrame(() => this.render());
            const box = this.scene.getObjectByName('box');
            box.rotation.x += 0.01;
            box.rotation.y += 0.01;


            this.renderer.render(this.scene, this.camera);
            this.stats.end();
        }

    }

    app = new App();
    app();

});
