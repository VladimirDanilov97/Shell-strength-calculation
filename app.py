from flask import Flask, request, render_template
from shell import Shell
from forms import ShellForm
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET','POST'])
def shell():
    form = ShellForm()
    context = {'form': form, 'Sr': None}
 
    print(form.data)
    if form.validate_on_submit():
        print('dfsdfsdfdsf')
        sh = Shell()
      
        sh.set_P(float(form.P.data))
        sh.set_T(float(form.T.data))
        sh.set_Dvn(float(form.Dvn.data))
        sh.set_steel(form.steel.data)
        sh.set_S(float(form.S.data))
        sh.set_C(float(form.C.data))
        sh.set_phi(float(form.phi.data))
        context['Sr'] = sh.calculate_Sr()

    return render_template('shell.html', **context)
    


if __name__ == '__main__':
    app.run(debug=True)