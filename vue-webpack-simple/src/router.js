import NavView from './views/Nav.vue'
import CodeView from './views/Code.vue'
import TaskView from './views/Task.vue'
import UserView from './views/User.vue'
import TaskActiveView from './views/TaskActive.vue'
import TaskMonitorView from './views/TaskMonitor.vue'
import TaskManageView from './views/TaskManage.vue'
import TaskForm from './components/TaskForm.vue'
import CodeNewView from './views/CodeNew.vue'


export default function(router) {
    router.map({
        '/task': {
            name: 'task',
            component: TaskView,
            subRoutes: {
                '/active': {
                    name: 'active',
                    component: TaskActiveView
                },
                '/monitor': {
                    name: 'monitor',
                    component: TaskMonitorView,
                },
                '/manage': {
                    name: 'manage',
                    component: TaskManageView
                },
                '/:_id': {
                    name: 'detail',
                    component: TaskForm
                }
            }
        },
        '/code': {
            name: 'code',
            component: CodeView,
            subRoutes: {
                '/new': {
                    name: 'new',
                    component: CodeNewView
                }
            }
        },
        '/user': {
            name: 'user',
            component: UserView
        }
    })
}