const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const video = document.querySelector('video');



startButton.addEventListener('click', async (e) => { 

    const display = await window.captureStream.getScreenUnderMouse();
    const sources = await window.captureStream.getSources();




    if (sources.length !==0) {
        for (const source of sources) {
            const button = document.createElement("button");
            button.textContent = source.name;


            console.log(`Source: ${source.name}, ID: ${source.id}`);

            button.addEventListener("click",  async () => { 

                try {
                    const stream = await navigator.mediaDevices.getUserMedia({
                        audio: false,
                        video: {
                            mandatory: {
                                chromeMediaSource: 'desktop',
                                chromeMediaSourceId: source.id  
                            }
                        }
                    });


                    const track = stream.getTracks().forEach(t =>)

                    

                    //console.log("stream-track:", stream.getTracks());

                    video.srcObject = stream;
                    await video.play();
                } catch (err) {
                    console.error('Could not start video source:', err);  // Shows DOMException
                }
                

            });

            const sourceContainer = document.getElementById("sourceContainer");
            sourceContainer.appendChild(button);
        }

    }
    

});


stopButton.addEventListener('click', () => {
    video.pause();
    
});