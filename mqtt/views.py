from django.shortcuts import render,redirect
import paho.mqtt.client as mqtt

# Create your views here.
def pub(request):
    return render(request, 'pub.html')


def publish(request):
    if request.method == "POST":
        topic = request.POST.get('topic','')
        message = request.POST.get('message','')

        mqttc = mqtt.Client(client_id="client", protocol=mqtt.MQTTv311)

        mqttc.connect("192.168.0.71",1883)
        mqttc.publish(topic, message, 2)
        print(f"Published to topic: {topic}, message: {message}")
        mqttc.loop_forever()

        return redirect('/mqtt/pub')